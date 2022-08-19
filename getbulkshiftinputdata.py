import openpyxl
# from openpyxl_datautils import CellRange

def get_bulk_shift_input_data(workbook: openpyxl.Workbook)->dict:
  input_sheet=workbook['Bulk_Shift_Input']
  return_value={'Bulk_Shift_days':None,'Monthly_rollup':'Yes','Quarterly_rollup':'No','Semi_Annual_rollup':'No','Annual_rollup':'Yes'}

  for val in input_sheet.values:
    if val[0] is not None and val[0].startswith('Bulk'):
      return_value['Bulk_Shift_days']=val[1]
      continue
    elif val[0] is not None and val[0].startswith('Monthly'):
      return_value['Monthly_rollup']=val[1]
      continue
    elif val[0] is not None and val[0].startswith('Quarterly'):
      return_value['Quarterly_rollup']=val[1]
      continue
    elif val[0] is not None and val[0].startswith('Semi-Annual'):
      return_value['Semi_Annual_rollup']=val[1]
      continue
    elif val[0] is not None and val[0].startswith('Annual'):
      return_value['Annual_rollup']=val[1]
      continue
  
  return return_value    
  
  # rows=inputsheets.rows
  
  # for i in range(5):
  



wbk=openpyxl.load_workbook("Prod_Prof.xlsx",read_only=True,data_only=True)


bulk_shift_options=get_bulk_shift_input_data(wbk)
print(bulk_shift_options)
print(type(bulk_shift_options.keys()))


if 'Bulk_Shift_days' in bulk_shift_options.keys():
  print(bulk_shift_options['Bulk_Shift_days'])
wbk.close()
