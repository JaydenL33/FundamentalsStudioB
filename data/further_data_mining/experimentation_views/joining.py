

def merge(df_list):
	merged = pd.merge(df_list[9],df_list[11],left_on='Numeric',right_on='cases', how='left')
	print(merged)
