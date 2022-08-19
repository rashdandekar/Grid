import openpyxl as xl
import pandas as pd
import read_xl_profile as rxp
import datetime
import scalecums

def get_data_for_scaling()->dict:
  # entity_types=['USERDF','SOURCE','SEP','TANK','JOINT','WELL','INLGEN']
  entity_types=['SEP']
  df_dict={}
  print("\nLoading workbook...\n")
  wbk=xl.load_workbook('Prod_Prof_scale.xlsx')
  for entity_type in entity_types:
    print(f"Starting to process {entity_type} sheet\n")
    # input_df=pd.DataFrame()
    # df=pd.read_excel(wbk,sheet_name=entity_type,header=[0,1],index_col=0,parse_dates=True,engine='openpyxl')
    input_df=pd.read_excel(wbk,sheet_name=entity_type,header=[0,1],index_col=0,engine='openpyxl')
    input_dates=input_df.index.to_numpy()
    input_df.index=input_dates
    input_df=rxp.get_required_columns(input_df)
    if not input_df.empty:
      df_dict[entity_type]=input_df
  wbk.close()
  return df_dict


def main()->None:
  data=get_data_for_scaling()
  print(data.keys())
  df=data[list(data.keys())[0]]
  # print(df.head())
  cols=df.columns.values
  data_values=df.values
  data_arrays=[[data_values[i,j] for i in range(len(data_values))] for j in range(len(cols))]
  dates_list=df.index.to_numpy()
  dates_list = [datetime.datetime.fromisoformat(x[0:len(x)-1]) for x in dates_list]
  
  # print(type(cols))
  # for col in cols:
  #   print(col)

  pass  
  
if __name__=='__main__':
  main()