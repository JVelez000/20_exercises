license = input("Do you have a license? (yes/no): ").lower()
helmet = input("Are you wearing a helmet? (yes/no): ").lower()
if license != "yes" or helmet != "yes":
  print("You cannot drive.")