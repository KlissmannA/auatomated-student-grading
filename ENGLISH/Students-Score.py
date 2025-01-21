import conn
import pandas as pd
import numpy as np
import emailconf
import time

query = 'SELECT * FROM info_students;'
df= pd.read_sql(query, con=conn.connection())

conn.connection().close()

df['total points'] = df['maths'] + df['science'] + df['art'] + df['history']  + df['biology']

df['total points'] = np.round(df['total points'],2)

df['avg points'] = np.where(
    (df['maths'] + df['science'] + df['art'] + df['history'] + df['biology']) == 0,
    0,
    (df['maths'] + df['science'] + df['art'] + df['history'] + df['biology']) / 5)

df['avg points'] = np.round(df['avg points'],2)

df_approved = df[df['avg points'] >= 75]

df_rejected = df[df['avg points'] < 75]

for index, row in df_approved.iterrows():
    recipient_email =  row['email']
    subject = f'Congratulations, {row['name']} {row['lastname']}, you have approved'
    body = f'''
    Hello {row['name']} {row['lastname']}, we wanted to congratulate you on your approval of the course.
    It is incredible what you have achieved. your score was:
    
    Maths: {row['maths']}  
    Science: {row['science']} 
    Art: {row['art']}
    History: {row['history']}
    Biology: {row['biology']}

    your total was:{row['total points']}

    your average was: {row['avg points']}

    Remember that it is approved with an average of 75 points or more.

    '''
    emailconf.email(recipient_email, subject, body)
    time.sleep(3)

for index, row in df_rejected.iterrows():
    recipient_email =  row['email']
    subject = f'{row['name']} {row['lastname']}, you are failed'
    body = f'''
    Hello {row['name']} {row['lastname']}, Unfortunately we want to inform you that you did not pass the course,
    your score was:
    
    Maths: {row['maths']}  
    Science: {row['science']} 
    Art: {row['art']}
    History: {row['history']}
    Biology: {row['biology']}

    your total was:{row['total points']}

    your average was: {row['avg points']}

    Remember that it is approved with an average of 75 points or more.

    '''
    emailconf.email(recipient_email, subject, body)
    time.sleep(3)