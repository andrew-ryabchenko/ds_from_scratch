salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]

# Bucket the tenures and return average salary per each bucket. 

bucket_avg = {'.<2':[], '2<=.<5':[], '.>=5':[]}

for s,t in salaries_and_tenures:
    if (t<2):
        bucket_avg['.<2'].append(s)
    elif (t<5):
        bucket_avg['2<=.<5'].append(s)
    else:
        bucket_avg['.>=5'].append(s)

for key in bucket_avg.keys():
    salaries=bucket_avg[key]
    print(f'Avg salary for {key} years: {sum(salaries)/len(salaries)}')
