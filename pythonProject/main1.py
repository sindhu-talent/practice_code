from helper import sales
obj=sales()
a=obj.read_data()
#print(a)
region_wise_df=obj.region_wise(a)
print(region_wise_df)
country_wise_df=obj.country_wise(a)
print(country_wise_df)


