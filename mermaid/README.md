

# Archi

``` mermaid
    graph TB
    subgraph block_1[-]
        direction LR
        subgraph group_A
            direction LR;

            A1[bob] --> A2 ;
        end
        subgraph group_B
            direction LR
            B1 --> B2
        end
        group_A ~~~ group_B
    end

    subgraph block_2[-]
        direction LR;
            subgraph group_C
            direction LR
                C1 --> C2
        end
            subgraph group_D
            direction LR
                D1 --> D2
        end
        group_C ~~~ group_D
    end

    block_1 ~~~ block_2


```

<!-- 
```mermaid
someID:::someClass

subgraph someID[Some Title]
    someItem(The subgraph title has some style)
end 

classdef someClass padding-left:5em;
``` -->


```mermaid
graph TB
    sq[Square shape] --> ci((Circle shape))

    subgraph A
        od>Odd shape]-- Two line<br/>edge comment --> ro
        di{Diamond with <br/> line break} -.-> ro(Rounded<br>square<br>shape)
        di==>ro2(Rounded square shape)
    end

    %% Notice that no text in shape are added here instead that is appended further down
    e --> od3>Really long text with linebreak<br>in an Odd shape]

    %% Comments after double percent signs
    e((Inner / circle<br>and some odd <br>special characters)) --> f(,.?!+-*ز)

    cyr[Cyrillic]-->cyr2((Circle shape Начало));

     classDef green fill:red,stroke:#333,stroke-width:2px;
     classDef orange fill:#f96,stroke:#333,stroke-width:4px;
     class sq,e green
     class di orange
```