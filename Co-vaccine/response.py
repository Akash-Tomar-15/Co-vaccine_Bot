import requests


def responses(input_text):
    finalstring = ''
    user_message = str(input_text).lower()

    if len(user_message) != 6:
        return 'Please enter valid PIN code!'

    x = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + user_message + "&date=5-10-2021")

    a = x.json()
    if len(a['centers']) != 0:
        for c in range(len(a['centers'])):
            centers = a['centers'][c]['address']
            state = a['centers'][c]['state_name']
            district = a['centers'][c]['district_name']
            block = a['centers'][c]['block_name']
            timings_from = a['centers'][c]['from']
            timings_to = a['centers'][c]['to']
            date = a['centers'][c]['sessions'][0]['date']
            available_dose = a['centers'][c]['sessions'][0]['available_capacity']
            age = a['centers'][c]['sessions'][0]['min_age_limit']
            vaccine = a['centers'][c]['sessions'][0]['vaccine']

            finalstring += "Centers: " + centers + '\n' + "State: " + state + '\n' + "District: " + district + '\n' + "Block: " + block + '\n' \
                           + "Timings From: " + timings_from + '\n' + "Timings to: " + timings_to + '\n' + "Date: " + date + '\n' \
                           + "Available Dose: " + str(available_dose)+'\n'+"Minimum Age: "+str(age)+'\n'+"Vaccine: "+vaccine + '\n' + '\n'
    else:
        finalstring = 'No vaccine center available for provided pin code. Please try for different pin code!'

    return finalstring
