
import cx_Oracle
import json

def credit_check(**args):
	
	SSN=args["SSN"]
	
	for check in args["json_data"]["credit_check"]:
		if check["SSN"] == args["SSN"]:

			connection=cx_Oracle.connect(user="stack_ras_sep23", password="stackinc", dsn="MKIT-DEV-OEM/APEXDB")

			cursor=connection.cursor()
			cursor.execute("""select * from credit_check where SSN=:SSN_INS """,
									SSN_INS=args["SSN"])
	
			return_score=cursor.fetchone()[1]
			cursor.close()
			if return_score:
				return return_score
			else:
				return None
	
if __name__ == "__main__":
	string_json="""
	{
			"credit_check":[
				{
					"FIRSTNAME": "John",
					"LASTNAME": "Doe",
					"AGE": 30,
					"SSN": "999-535-2353",
					"ADDRESS": "102 peach rd"
    			},
  				{
					"FIRSTNAME": "Jane",
					"LASTNAME": "Smith",
					"AGE": 25,
					"SSN": "999-923-4575",
					"ADDRESS": "437 bum st"
				},

				{
					"FIRSTNAME": "Bob",
					"LASTNAME": "Johnson",
					"AGE": 40,
					"SSN": "999-924-1367",
					"ADDRESS":"234 CRITTER ROAD"
				}
			]
	}		
	"""
	

	json_data=json.loads(string_json)
	
	SSN=input("Enter SSN: ")

		

	return_score=credit_check(json_data=json_data,SSN=SSN)
	
	# Display result
	if return_score is not None:
			if return_score > 720:
				print("Approved")
			else:
				print("Denied")
	else:
		print("%s not found"%(SSN))
