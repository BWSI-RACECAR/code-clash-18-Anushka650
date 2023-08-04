"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make
a Talking Clock? I need a script that takes an input 24-hour time
(00:00 - 23:59) and translates it into words. Please format the input
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
TIMES = { 1:'one', 2:'two',
        3:'three', 4:'four', 5:'five',
        6:'six', 7:'seven', 8:'eight',
        9:'nine', 10:'ten', 11:'eleven',
        12:'twelve', 13:'thirteen', 14:'fourteen',
        15:'fifteen', 16:'sixteen', 17:'seventeen',
        18:'eighteen', 19:'nineteen', 20:'twenty',
        21:'twenty one', 22:'twenty two', 23:'twenty three',
        24:'twenty four', 25:'twenty five', 26:'twenty six',
        27:'twenty seven', 28:'twenty eight', 29:'twenty nine',
        30:'thirty',31:'thirty one', 32:'thirty two',
        33:'thirty three', 34:'thirty four', 35:'thirty five',
        36:'thirty six', 37:'thirty seven', 38:'thirty eight', 39:'thirty nine',
        40:'forty', 41:'forty one', 42:'forty two', 43:'forty three',
        44:'forty four', 45:'forty five',
        46:'forty six', 47:'forty seven', 48:'forty eight',
        49:'forty nine', 50:'fifty', 51:'fifty one',
        52:'fifty two', 53:'fifty three', 54:'fifty four',
        55:'fifty five', 56:'fifty six', 57:'fifty seven',
        58:'fifty eight', 59:'fifty nine'}

class Solution:
    def ClockTalker(self, input_time):
        hours, minutes = map(int, input_time.split(':'))
        if hours == 0:
            regular_hours = 12
            period = 'am'
        elif 1 <= hours <= 11:
            regular_hours = hours
            period = 'am'
        elif hours == 12:
            regular_hours = 12
            period = 'pm'
        else:
            regular_hours = hours - 12
            period = 'pm'

        if minutes == 0:
            minute_str = ''
        elif minutes <= 9:
            minute_str = 'oh ' + TIMES[minutes]
        else:
            minute_str = TIMES[minutes]

        output_str = f"It's {TIMES[regular_hours]} {minute_str} {period}"
        return output_str

            #type input_time: string
            #return type: string

            #TODO: Write code below to return a string with the solution to the prompt.


def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)

if __name__ == '__main__':
    main()

