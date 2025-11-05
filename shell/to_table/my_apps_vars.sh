# env_letter=${my_app_env:0:1}
# # env_letter=$(hostname)

# location=${location:-paris}
the_path="/root/$my_app_env/$location/very long chemin"
database=${database:-${my_app_env}_db}
# database=${database^^}: