> colorized sections describing yaml or json are not copy-pastable as is.

\- $`\textcolor{red}{\text{hostname}}`$: host_1  
   os: linux  
   cost: 5000  
   state: alive  
   env: qua  

---
regions:  
  west coast:  
    dc:  
      dc_a:  
      - { hostname: host_a_1, os: linux, state: alive }  
      - { hostname: host_a_2, os: linux, state: "unreachable" }  
      - { hostname: host_a_3, os: linux, state: alive }  
