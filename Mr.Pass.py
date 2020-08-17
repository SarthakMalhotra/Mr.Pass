import random
import string
import os
import sys

def logo():
	print """

MMMMMMMM               MMMMMMMM                            PPPPPPPPPPPPPPPPP                                                    
M:::::::M             M:::::::M                            P::::::::::::::::P                                                   
M::::::::M           M::::::::M                            P::::::PPPPPP:::::P                                                  
M:::::::::M         M:::::::::M                            PP:::::P     P:::::P                                                 
M::::::::::M       M::::::::::Mrrrrr   rrrrrrrrr             P::::P     P:::::Paaaaaaaaaaaaa      ssssssssss       ssssssssss   
M:::::::::::M     M:::::::::::Mr::::rrr:::::::::r            P::::P     P:::::Pa::::::::::::a   ss::::::::::s    ss::::::::::s  
M:::::::M::::M   M::::M:::::::Mr:::::::::::::::::r           P::::PPPPPP:::::P aaaaaaaaa:::::ass:::::::::::::s ss:::::::::::::s 
M::::::M M::::M M::::M M::::::Mrr::::::rrrrr::::::r          P:::::::::::::PP           a::::as::::::ssss:::::ss::::::ssss:::::s
M::::::M  M::::M::::M  M::::::M r:::::r     r:::::r          P::::PPPPPPPPP      aaaaaaa:::::a s:::::s  ssssss  s:::::s  ssssss 
M::::::M   M:::::::M   M::::::M r:::::r     rrrrrrr          P::::P            aa::::::::::::a   s::::::s         s::::::s      
M::::::M    M:::::M    M::::::M r:::::r                      P::::P           a::::aaaa::::::a      s::::::s         s::::::s   
M::::::M     MMMMM     M::::::M r:::::r                      P::::P          a::::a    a:::::assssss   s:::::s ssssss   s:::::s 
M::::::M               M::::::M r:::::r                    PP::::::PP        a::::a    a:::::as:::::ssss::::::ss:::::ssss::::::s
M::::::M               M::::::M r:::::r                    P::::::::P        a:::::aaaa::::::as::::::::::::::s s::::::::::::::s 
M::::::M               M::::::M r:::::r                    P::::::::P         a::::::::::aa:::as:::::::::::ss   s:::::::::::ss  
MMMMMMMM               MMMMMMMM rrrrrrr                    PPPPPPPPPP          aaaaaaaaaa  aaaa sssssssssss      sssssssssss    
                                                                                                                         
                                                                                                                         """
os.system("clear")
logo()
# printing lowercase

print "Press Enter To Generate Password "
print "Press Ctrl + z To Exit"
a=raw_input("")
if a == '':
	print ("Your Password : ")
	letters = string.ascii_lowercase
	print ( ''.join(random.choice(letters) for i in range(10)) )
#Generated Successfully