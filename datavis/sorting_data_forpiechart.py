import json

with open('cancer.json') as f:
   data = json.load(f)

edge_dict = data["edge-dict"]
first_value = 1

for key, value in edge_dict.items():
   if len(value) > first_value:
      max_value = len(value)
      first_value = len(value)

print(max_value)

# results ={2105 1
# 3539 1
# 2120 1
# 2565 1
# 1442 1
# 1443 1
# 3708 3
# 1529 1
# 3446 2
# 3738 2
# 3677 5
# 3485 2
# 3720 2
# 3631 2
# 1663 1
# 3278 2
# 3852 4
# 3246 3
# 3492 3
# 1669 1
# 3251 3
# 1671 1
# 3957 6
# 1673 1
# 2899 2
# 2840 2
# 1676 1
# 1677 1
# 3397 3
# 2253 1
# 3931 2
# 3772 1
# 3160 3
# 3780 2
# 2309 2
# 3781 1
# 3250 3
# 3249 2
# 3709 2
# 3823 2
# 1868 1
# 1869 1
# 3335 2
# 1871 1
# 3522 1
# 1875 1
# 1879 1
# 1880 1
# 2441 1
# 1883 1
# 1884 1
# 3782 1
# 1886 1
# 1887 1
# 1888 1
# 2809 2
# 3204 2
# 3580 1
# 1894 1
# 2842 1
# 1896 1
# 2217 1
# 2219 1
# 2220 1
# 3248 2
# 3523 1
# 3159 2
# 3390 2
# 2306 1
# 2307 1
# 3162 3
# 3576 1
# 3577 1
# 3578 1
# 3211 1
# 3210 1
# 3268 3
# 2824 1
# 2827 1
# 2896 1
# 3317 3
# 3806 3
# 2907 1
# 2905 1
# 3548 1
# 3895 1
# 3921 1
# 3048 1
# 3054 1
# 3120 1
# 3119 1
# 3839 1
# 3161 1
# 3252 1
# 3357 1
# 3266 1
# 3271 1
# 3274 1
# 3325 2
# 3824 2
# 3324 2
# 3281 1
# 3396 1
# 3393 1
# 3388 1
# 3391 1
# 3392 1
# 3395 1
# 3398 1
# 3828 1
# 3491 1
# 3494 1
# 3739 1
# 3744 1
# 3745 1
# 3746 1
# 3747 1
# 3748 1
# 3743 1
# 3854 1
# 3853 1
# 3855 1}