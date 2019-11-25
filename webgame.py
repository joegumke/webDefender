#!/usr/bin/python3
import curses,random
from random import choice
from string import ascii_lowercase
#stdscr = curses.initscr()
#curses.noecho()

# Author: Joe Gumke
# Date : 11-24-18
# Name : webgame.py
# Description : Game created in order to educate users on methods to attack/defend a public site/service

# *** TO DO ***
# Build Money Generator
# Build Chance Calculator
# Build Attack Chance calculator
# Build Tool Selection
# Build Business Line Requirements 
# Site Statistics Generator (speed/uptime/monitoring)
# Build Issue Generator

# additional exampels
# on prem vs cloud
# misconfigured systems -- open ports / outdated software / unneccesary software running
# misconfiguerd cloud firewall
# no monitooring configured for cloud products



issues_general =["Site getting Denial of Service","Site went down","Site was defaced","Site was deleted",'Site populating strange code','Site was found to contain cross side scripting code','Site getting distributed denial of service','Site getting scanned/probed externally frequently','Site getting brute forced from public facing port showing SSH port on the internet','DNS Misconfiguration','SMTP misconfiguration']

issues_financial =["Site getting numerous accounts of fraud",'site incorrectly authenticating users','Site not properly authenticating users','Site is getting mobile fraud occurring']

issues_socialMedia = ["Site is getting threats published on several pages",'Pages are populating cross side scripting','Site is getting spammed by bots publishing garbage content']

firewallStat = 0
idsStat = 0 
ddosStat = 0

# tools_upgrade_path = ['firewall':
# firewall : first generation : packet filters --  Second Generation >> stateful filters -- Third Generation ->>  application layer
firewall_set = {'firstgeneration':500, 'secondgeneration':1000, 'thirdgeneration':2000}
# ids : ids > ips > signature based detection > statistical anomaly detection > stateful protocol analysis
ids_set = {'ids':500,'ips-sig':1000,'ips-statistical':1500,'ips-stateful':2000}
# ddos : akamai , cloudflare, aws , azure
ddos_set = {'akamai':5000,'cloudflare':6000,'aws':7000,'azure':8000}

gameCompletion = 0
money = 1000.00
userStats=[]
print("Welcome To The Web Defender Game...")
print("Objective: You have a Corp Web Site to protect.\r\nCurrently its a basic html site.\r\nBusiness Lines will present needs to publish public services for generating revenue.\r\nThese services must be protected...\r\nGood Luck...")

raw_input('Press Enter to Continue...')

print('Initial Funds : $%.2f' % money)
print('Initial Issues',choice(issues_general))
print ("Purchase a Tool to help mitigate attacks")

def riskScore():
    attack = random.randint(0, 100)
    print ("Attack Chance : %s%%" % attack)

def moneyRemove(stat):
    money = money - stat
def moneyAdd(stat):
    money = money + stat

def userAttributesAdd(userStats,userValue):
    userStats.append(userValue)
def userAttrituesRemove(userStats,userValue):
    userStats.remove(userValue)

def choiceSelection(dataset):
    loopCount = 0
    for key,value in dataset.items():
        print loopCount,key,value
        loopCount +=1
    choice = raw_input("Select Option To Upgrade or 'Q' To Quit...")
    test = choice.isdigit()
    print(test)
    loopFinalCount = loopCount - 1
    if ( test == False):
        if (choice in ['Q','q']):
            exit()
        if (choice not in ['Q','q']):
            choiceSelection(dataset)
    else: 
        if (int(choice) < loopFinalCount):
            print(dataset[choice])
            print(dataset[key])
            moneyRemove(value[choice])
            print(money)

#riskScore()
choiceSelection(firewall_set)
print userStats
