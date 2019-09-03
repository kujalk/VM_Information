
#Purpose - To create static html web pages from CSV files
#Developer - Janarthanan
#Date - 28/8/2019

import csv
import sys
from datetime import datetime

def Get_Html(server,csv_file,html_file):
    # Open the CSV file for reading
    reader = csv.reader(open(csv_file))

    # Create the HTML file
    f_html = open(html_file,"w");

    section_1="""
    <html>
    <body>
    <div style="height: 90;size: 80;background-color:cyan">
    <p style="color: black;font-size: 40;text-align: center;padding-top: 30;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif">VMs INFORMATION ACROSS SERVERS</p>
    </div >
    <div style="height: 45;size: 40;background-color:lightskyblue">
        <label style="font-size: 25;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif">
    """

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    section_2="Date & Time: "+dt_string

    section_3="""
    </label>
        <label style="font-size: 25;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;text-align: right;padding-left: 250">

    """

    section_4="Server : "+server

    section_5="""
    </label>
    </div>
    <div style="height: 45;size: 40;padding-top: 10">
        <table  style='font-style: bold; color:black; font-family:serif; font-size: 20px;'>

            <tr>
                <td width="40%"> <a href="server_201.html">Server 201</a></td>
                <td width="40%"> <a href="server_202.html">Server 202</a></td>
                <td width="40%"> <a href="server_203.html">Server 203</a></td>
    </div>
    """
    f_html.write(section_1)
    f_html.write(section_2)
    f_html.write(section_3)
    f_html.write(section_4)
    f_html.write(section_5)
    f_html.write('<title>VM Information</title>')
    f_html.write("""<table border="1" style='font-style: bold; color:black; font-family:courier; font-size: 16px;'>""")

    header=0
    
    for row in reader: # Read a single row from the CSV file

        col=0
        f_html.write('<tr>')
        for column in row: # For each column..
            if(header==0):
                #print ("Headers : "+column )
                f_html.write("""<td height="40" style="background-color: bisque;font-size: 20;color:red;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">""" + column + '</td>')
            else:
                if(col==2):
                    values=column.replace(" "," | " )
                    #print("column : "+values)
                    f_html.write("""<td height="25" style="background-color: bisque;font-size: 17;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">"""+ values + '</td>')
                else:
                    #print("column : "+column )
                    f_html.write("""<td height="25" style="background-color: bisque;font-size: 17;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">""" + column + '</td>')

            col+=1

        f_html.write('</tr>')
        header+=1

    f_html.write("""</table></body></html>""")
    f_html.close()


#Calling CSV for server 201,202 and 203

Get_Html("Server 101","/Jana_Scripts/csv_files/192.168.2.101.csv","/var/www/html/server_101.html")
Get_Html("Server 102","/Jana_Scripts/csv_files/192.168.2.102.csv","/var/www/html/server_102.html")
Get_Html("Server 103","/Jana_Scripts/csv_files/192.168.2.103.csv","/var/www/html/server_103.html")



