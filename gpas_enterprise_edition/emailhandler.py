import smtplib
import datetime as dt

def email_trigger(sec_pattern,RECIVER):
  CURR_TIME = dt.datetime.now
  try :
    print(sec_pattern)
    print(RECIVER)
    print(CURR_TIME)
    email_sender(sec_pattern,RECIVER,CURR_TIME)
  except Exception as e:
        print("The error is: ",e)
     
   

def email_sender(sec_pattern,RECIVER,CURR_TIME) :
    
    MY_EMAIL = "your email"
    PASSWORD = "your passkey"
    MASSAGE = f"""
    Hello dear user,
      OTP pattern generated at time =  {CURR_TIME}
      
      PATTERN = {sec_pattern}

      id not you please contact and change password

      thank you !
    """
    try :
      with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECIVER,
                            msg=MASSAGE
                            )
      # return 0
    
    except Exception as e:
        print("The error is: ",e)
        # return -1 
       
# sec = [[1,2],[1,3],[3,1],[0,0],[0,0]]
# email_trigger(sec,"professional0012345@gmail.com")
