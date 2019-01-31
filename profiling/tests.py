import pandas as pd
df = pd.read_csv("objects_description.csv", "objects_description")
for index, row in df.iterrows():
    cur = str(row.values[0]).split(',')
    print(cur)
    # if len(cur) == 5:
    #     print(2)
    #     device = Device()
    #     device.pk = cur[0]
    #     user, created = User.objects.get_or_create(pk=cur[1])
    #     device.user = user
    #     device.type = cur[2]
    #     device.brand = cur[3]
    #     device.model = cur[4]
    #     device.save()
    # break