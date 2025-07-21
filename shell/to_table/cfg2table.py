#!/usr/bin/env python3

import os
import argparse
import tabulate
import json

parser = argparse.ArgumentParser(description='Transform config to table',add_help=False)
parser.add_argument("-h", "--help",nargs="*", help = "Show this help")
parser.add_argument("-i", "--conf_base_name", help = "conf_base_name")
parser.add_argument("-f", "--format", help = "formats")
parser.add_argument("-s", "--select", help = "Select Fields")

args = parser.parse_args()
if args.help:
    parser.print_help()
    exit(0)

if not args.conf_base_name:
    print("Error: conf_base_name is required")
    parser.print_help()
    exit(1)

if not args.format:
    args.format = 'simple'
tabulate_formats = tabulate._table_formats.keys()
all_formats = list(tabulate_formats) + ['json'] + ['gitlab_json_table']
if not args.format  in all_formats:
    print(f"Error: Invalid format '{args.format}'. Available formats are:\n{', '.join(tabulate_formats)}")
    exit(2)


files = [f for f in os.listdir('.') if f.startswith(args.conf_base_name)]
for f in files:
    print(f)


base_path=(f'{"/".join(args.conf_base_name.split("/")[:-1])}')
base_name=(f'{args.conf_base_name.split("/")[-1]}')


if not os.path.exists(base_path):
    print(f"Error: Base path '{base_path}' does not exist.")
    exit(1)

prefixed = [entry for entry in os.listdir(base_path) if entry.startswith(base_name) and os.path.isfile(os.path.join(base_path, entry))]

dataset = {}
all_keys = []
for file_name in prefixed:
    file_path = os.path.join(base_path, file_name)
    group=f"{file_name.split('.')[0].split('_')[-1]}"
    if file_name.endswith('.cfg'):
        with open(file_path, 'r') as f:
            input_data = f.read()
    group_dataset = {}
    for row in input_data.splitlines():
        if row.startswith('#') or not row:
            continue
        key, value = row.split('=', 1)
        group_dataset.update({key: value})
        if key not in all_keys:
            all_keys.append(key)
    dataset[group] = group_dataset

all_keys.sort()
final_dataset = {}
final_list = []

if args.select:
    fields = args.select.split(',')
else:
    fields = list(dataset)


# print(dataset)
# exit(0)

for key in all_keys:
    final_dataset[key] = {}
    # for field in fields:
    for group, data in dataset.items():
        # group = field
        # data = dataset[group]
        if group in fields:
            final_dataset[key][group] = data.get(key, "")
    final_list.append([key] + [final_dataset[key][group] for group in fields])

gitlab_json_table_out = []
for key, value in final_dataset.items():
    record = {"key": key, **value}
    gitlab_json_table_out.append(record)

# print(json.dumps(gitlab_json_table_out, indent=4))
# exit(0)

if args.format == "gitlab_json_table":
    gitlab_json_table_out = []
    for key, value in final_dataset.items():
        record = {"key": key, **value}
        gitlab_json_table_out.append(record)

    out_dataset = {
        # "fields": fields,
        "fields": [ { "key": key, "sortable": "true" } for key in fields ],
        "items": gitlab_json_table_out,
        "filter": True,
        "caption": f"{args.conf_base_name}"
    }
    # print('```json:table\n')
    print(f"```json:table\n{json.dumps(out_dataset,indent=2, separators=(',', ': '))}\n```")
    # print('```\n')
elif args.format == 'json':
    print(json.dumps(final_dataset, indent=4))
else:
    print(tabulate.tabulate(final_list, headers=["Key"] + fields , tablefmt=args.format))

