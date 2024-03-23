def add_time(start, duration, w = False):
  
  start_time = start.split()
  start_h = int(start_time[0].split(':')[0])
  start_min = int(start_time[0].split(':')[1])
  AM_PM = start_time[1]
  duration_h = int(duration.split(':')[0])
  duration_min = int(duration.split(':')[1])
  

  week = ['Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']

  
  
  
  hs = start_h + duration_h
  min = start_min + duration_min

  total_hs = hs + int(min/60)
  if AM_PM == 'PM':
    total_hs += 12
  total_min = min % 60
  if total_min < 10:
    total_min = '0' + str(total_min)
  
  days = int(total_hs / 24)
  final_hs = total_hs % 24
#final_hs is in 24 hs format



#If a day of the week is given calculate the day of the week of the result
  if w:
    we = w.title()
    index = week.index(we)
    index += days
    index = index % 7
    f_week = week[index]
      
    
  

  PM = ''
  if final_hs >= 12:
    PM = 'PM'
  else:
    PM = 'AM'


#turning final_hs into 12 hs format
  if final_hs > 12:
    final_hs -= 12
  if final_hs == 0:
    final_hs = 12
  

  new_time = str(final_hs) + ':' + str(total_min) + ' ' + PM

  if w:
    new_time += ', ' + f_week
    
  if days == 1:
    new_time += ' (next day)'
  elif days > 1:
    new_time += ' (' + str(days) + ' days later)'

  
  return new_time