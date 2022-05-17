#!/usr/bin/evn python3
# encoding: utf-8

# [Github] www.github.com/GMagNLL
# [Telegram - Channel] t.me/joinchat/AAAAAEANZwsT9F2Y-aBVIQ
# 
# [License]
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

__author__ = 'Zwdeff'
__version__ = '0.2'
import random
import os, sys

from time import sleep
from os import system

n0 = '\033[90m'
n1 = '\033[31m'
n2 = '\033[32m'
n3 = '\033[33m'
n4 = '\033[94m'
n5 = '\033[34;1m'
n6 = '\033[96m'
n7 = '\033[97m'

Banner = '''
 ____  _            ____
|  _ \| |__   ___  / ___| ___ _ __
| |_) | '_ \ / _ \| |  _ / _ \ '__|
|  __/| | | | (_) | |_| |  __/ |
|_|   |_| |_|\___/ \____|\___|_|'''

print(n4+Banner+'\033[m')
print(n4+'Generate_Random_Phone_Number\n\033[m')
print(n4+' |---- :'+n5+' Author  : %s\033[m' %(__author__))
print(n4+' |---- :'+n5+' Version : %s\n\033[m' %(__version__))

def case():
 try:
    print (n4+'\n1) = Numeros 9 Digitos\033[m')
    print (n4+'0) = Exit\n\n\033[m')
    
    nb = input(n5+'[noob] :: ')
    while nb != '1' or nb != '2' or nb != '0':
       if nb == '1' or nb == '2' or nb == '0':
          if nb == '0':
             print (n1+'\nGoing Out ..\033[m')
             sleep(2)
             exit()
          if nb == '1':
           def dig9():
               count = 0
               print(n4+'Categories [:]')
               print(n4+'1) = 999999XXX')
               print(n4+'2) = 99999XXXX')
               print(n4+'3) = 9999XXXXX')
               print(n4+'4) = 999XXXXXX')
               print(n4+'5) = 99XXXXXXX')
               print(n4+'6) = 99XXXXXX9')
               print(n4+'7) = 99XXXXX99')
               print(n4+'8) = 99XXXX999')
               print(n4+'9) = 99XXX9999')
               print(n4+'0) = Home\n\033[m')
               
               slct = input(n5+'[noob] :: ')
               if slct == '0':
                  case()
               if slct == '1':
                  def Ger1(arg, count, arq):
                      vn = input(n4+'[xxxxxx]XXX <<< 6 Primeiros Numeros :: ')
                      dD = input(n4+'DDD desejado Ex: 062 :: ')
                      nx = int(input(n4+'Quantos numeros voce quer Gerar 1/1000 :: '))
                      print(n5+'Gerando Numeros no Arquivo %s [:]\033[m' %(arq.name))
                      sleep(2)
                      for i in range(nx):
                          a1 = random.randrange(0, 10)
                          b1 = random.randrange(0, 10)
                          c1 = random.randrange(0, 10)
                          count = count +1
                          
                          arq.write(str(dD)+str(vn)+str(a1)+str(b1)+str(c1)+'\n')
                          print(n4+str(dD)+str(vn)+str(a1)+str(b1)+str(c1)+'\033[m')
                      
                          if count == nx:
                             arq.close()
                             dig9()
                             
               if slct == '2':
                  def Ger2(arg, count, arq):
                      vn = input(n4+'[xxxxx]XXXX <<< 5 Primeiros Numeros :: ')
                      dD = input(n4+'DDD desejado Ex: 062 :: ')
                      nx = int(input(n4+'Quantos numeros voce quer Gerar 1/10000 :: '))
                      print(n5+'Gerando Numeros no Arquivo %s [:]\033[m' %(arq.name))
                      sleep(2)
                      for i in range(nx):
                          a1 = random.randrange(0, 10)
                          b1 = random.randrange(0, 10)
                          c1 = random.randrange(0, 10)
                          d1 = random.randrange(0, 10)
                          count = count +1
                          
                          arq.write(str(dD)+str(vn)+str(a1)+str(b1)+str(c1)+str(d1)+'\n')
                          print(n4+str(dD)+str(vn)+str(a1)+str(b1)+str(c1)+str(d1)+'\033[m')
                          if count == nx:
                             arq.close()
                             dig9()
                             
               if slct == '3':
                  def Ger3(arg, count, arq):
                      vn = input(n4+'[xxxx]XXXXX <<< 4 Primeiros Numeros :: ')
                      dD = input(n4+'DDD desejado Ex: 062 :: ')
                      nx = int(input(n4+'Quantos numeros voce quer Gerar 1/20000 :: '))
                      print(n5+'Gerando Numeros no Arquivo %s [:]\033[m' %(arq.name))
                      sleep(2)
                      for i in range(nx):
                          a1 = random.randrange(0, 10)
                          b1 = random.randrange(0, 10)
                          c1 = random.randrange(0, 10)
                          d1 = random.randrange(0, 10)
                          e1 = random.randrange(0, 10)
                          count = count +1
                          
                          arq.write(str(dD)+str(vn)+str(a1)+str(b1)+str(c1)\
                                   +str(d1)+str(e1)+'\n')
                          print (n4+str(dD)+str(vn)+str(a1)+str(b1)+str(c1)+str(d1)+str(e1)\
                               +'\033[m')
                          if count == nx:
                             arq.close()
                             dig9()
                             
               if slct == '4':
                  def Ger4(arg, count, arq):
                      vn = input(n4+'[xxx]XXXXXX <<< 3 Primeiros Numeros :: ')
                      dD = input(n4+'DDD desejado Ex: 062 :: ')
                      nx = int(input(n4+'Quantos numeros voce quer Gerar 1/30000 :: '))
                      print(n5+'Gerando Numeros no Arquivo %s [:]\033[m' %(arq.name))
                      sleep(2)
                      for i in range(nx):
                          a1 = random.randrange(0, 10)
                          b1 = random.randrange(0, 10)
                          c1 = random.randrange(0, 10)
                          d1 = random.randrange(0, 10)
                          e1 = random.randrange(0, 10)
                          f1 = random.randrange(0, 10)
                          count = count +1
                          
                          arq.write(str(dD)+str(vn)+str(a1)+str(b1)+str(c1)\
                                   +str(d1)+str(e1)+str(f1)+'\n')
                          print(n4+str(dD)+str(vn)+str(a1)+str(b1)+str(c1)\
                               +str(d1)+str(e1)+str(f1)+'\033[m')
                          if count == nx:
                             arq.close()
                             dig9()
               
               if slct == '5':
                  def Ger5(arg, count, arq):
                      vn = input(n4+'[xx]XXXXXXX <<< 2 Primeiros Numeros :: ')
                      dD = input(n4+'DDD desejado Ex: 062 :: ')
                      nx = int(input(n4+'Quantos numeros voce quer Gerar 1/40000 :: '))
                      print(n5+'Gerando Numeros no Arquivo %s [:]\033[m' %(arq.name))
                      sleep(2)
                      for i in range(nx):
                          a1 = random.randrange(0, 10)
                          b1 = random.randrange(0, 10)
                          c1 = random.randrange(0, 10)
                          d1 = random.randrange(0, 10)
                          e1 = random.randrange(0, 10)
                          f1 = random.randrange(0, 10)
                          g1 = random.randrange(0, 10)
                          count = count +1
                          
                          arq.write(str(dD)+str(vn)+str(a1)+str(b1)+str(c1)\
                                   +str(d1)+str(e1)+str(f1)+str(g1)+'\n')
                          print(n4+str(dD)+str(vn)+str(a1)+str(b1)+str(c1)\
                               +str(d1)+str(e1)+str(f1)+str(g1)+'\033[m')
                          if count == nx:
                             arq.close()
                             dig9()
                             
               if slct == '6':
                  def Ger6(arg, count, arq):
                      vn = input(n4+'[xx]XXXXXX[x] <<< 2 Primeiros, e Ultimo Ex: 98 8 :: ')
                      if ' ' in v:
                         n = v[0]+v[1]
                         v = v[3]+v[4]
                      else:
                         print(n1+'Error: Utilize 3 Numeros Separadamente 2/1 Ex: 98 8\033[m')
                         Ger9(arg, count, arq)
                      if int(n) > 99 or int(n) < 10 or int(v) < 10 or int(v) > 99:
                         print(n1+'Error: Utilize 3 Numeros Separadamente 2/1 Ex: 98 8\033[m')
                         Ger6(arg, count, arq)
                      dD = input(n4+'DDD desejado Ex: 062 :: ')
                      nx = int(input(n4+'Quantos numeros voce quer Gerar 1/30000 :: '))
                      print(n5+'Gerando Numeros no Arquivo %s [:]\033[m' %(arq.name))
                      sleep(2)
                      for i in range(nx):
                          a1 = random.randrange(0, 10)
                          b1 = random.randrange(0, 10)
                          c1 = random.randrange(0, 10)
                          d1 = random.randrange(0, 10)
                          e1 = random.randrange(0, 10)
                          f1 = random.randrange(0, 10)
                          count = count +1
                          
                          arq.write(str(dD)+str(n)+str(a1)+str(b1)+str(c1)\
                                   +str(d1)+str(e1)+str(f1)+str(v)+'\n')
                          print(n4+str(dD)+str(n)+str(a1)+str(b1)+str(c1)+\
                                +str(d1)+str(e1)+str(f1)+str(v)+'\033[m')
                          if count == nx:
                             arq.close()
                             dig9()
                             
               if slct == '7':
                  def Ger7(arg, count, arq):
                      vn = input(n4+'[xx]XXXXX[xx] <<< 2 Primeiros, e 2 Ultimos Ex: 98 88 :: ')
                      dD = input(n4+'DDD desejado Ex: 062 :: ')
                      if ' ' in v:
                         n = v[0]+v[1]
                         v = v[3]+v[4]
                      else:
                         print(n1+'Error: Utilize 4 Numeros Separadamente 2/2 Ex: 98 88\033[m')
                         Ger9(arg, count, arq)
                      if int(n) > 99 or int(n) < 10 or int(v) < 10 or int(v) > 99:
                         print(n1+'Error: Utilize 4 Numeros Separadamente 2/2 Ex: 98 88\033[m')
                         Ger7(arg, count, arq)
                      nx = int(input(n4+'Quantos numeros voce quer Gerar 1/20000 :: '))
                      print(n5+'Gerando Numeros no Arquivo %s [:]\033[m' %(arq.name))
                      sleep(2)
                      for i in range(nx):
                          a1 = random.randrange(0, 10)
                          b1 = random.randrange(0, 10)
                          c1 = random.randrange(0, 10)
                          d1 = random.randrange(0, 10)
                          e1 = random.randrange(0, 10)

                          count = count +1
                          arq.write(str(dD)+str(n)+str(a1)+str(b1)+str(c1)\
                                   +str(d1)+str(e1)+str(v)+'\n')
                          print(n4+str(dD)+str(n)+str(a1)+str(b1)+str(c1)\
                               +str(d1)+str(e1)+str(v)+'\033[m')
                          if count == nx:
                             arq.close()
                             dig9()
                             
               if slct == '8':
                  def Ger8(arg, count, arq):
                      vn = input(n4+'[xx]XXXX[xxx] <<< 2 Primeiros, e 3 Ultimos Ex: 98 885 :: ')
                      dD = input(n4+'DDD desejado Ex: 062 :: ')
                      if ' ' in v:
                         n = v[0]+v[1]
                         v = v[3]+v[4]+v[5]
                      else:
                         print(n1+'Error: Utilize 5 Numeros Separadamente 2/3 Ex: 98'\
                              +' 885\033[m')
                         Ger9(arg, count, arq)
                      if int(n) > 99 or int(n) < 10 or int(v) < 100\
                       or int(v) > 999:
                         print (n1+'Error: Utilize 5 Numeros Separadamente 2/3 Ex: 98'\
                               +' 885\033[m')
                         Ger8(arg, count, arq)
                      nx = int(input(n4+'Quantos numeros voce quer Gerar 1/10000 :: '))
                      print(n5+'Gerando Numeros no Arquivo %s [:]\033[m' %(arq.name))
                      sleep(2)
                      for i in range(nx):
                          a1 = random.randrange(0, 10)
                          b1 = random.randrange(0, 10)
                          c1 = random.randrange(0, 10)
                          d1 = random.randrange(0, 10)
                          
                          count = count +1
                          arq.write(str(dD)+str(n)+str(a1)+str(b1)+str(c1)\
                                   +str(d1)+str(v)+'\n')
                          print(n4+str(dD)+str(n)+str(a1)+str(b1)+str(c1)+str(d1)+str(v)\
                               +'\033[m')
                          if count == nx:
                             arq.close()
                             dig9()
               if slct == '9':
                  def Ger9(arg, count, arq):
                      v = input(n4+'[xx]XXX[xxxx] <<< 2 Primeiros, e 4 Ultimos Ex: 98 8857'\
                                +' :: ')
                                
                      if ' ' in v:
                         n = v[0]+v[1]
                         v = v[3]+v[4]+v[5]+v[6]
                      else:
                         print(n1+'Error: Utilize 6 Numeros Separadamente 2/4 Ex: 98'\
                              +' 8857\033[m')
                         Ger9(arg, count, arq)
                      if int(n) > 99 or int(n) < 10 or v == '' or int(v) < 1000\
                       or int(v) > 9999:
                         print(n1+'Error: Utilize 6 Numeros Separadamente 2/4 Ex: 98'\
                              +' 8857\033[m')
                         Ger9(arg, count, arq)
                      dD = input(n4+'DDD desejado Ex: 062 :: ')
                      nx = int(input(n4+'Quantos numeros voce quer Gerar 1/1000 :: '))
                      print(n5+'Gerando Numeros no Arquivo %s [:]\033[m' %(arq.name))
                      sleep(2)
                      for i in range(nx):
                          a1 = random.randrange(0, 10)
                          b1 = random.randrange(0, 10)
                          c1 = random.randrange(0, 10)

                          count = count +1
                          arq.write(str(dD)+str(n)+str(a1)+str(b1)+str(c1)+str(v)+'\n')
                          print(n4+str(dD)+str(n)+str(a1)+str(b1)+str(c1)+str(v)+'\033[m')
                          if count == nx:
                             arq.close()
                             dig9()
                             
               def ar(count, slct):
                   print(n5+'Crie um Arquivo para Guardar os Numeros\033[m')
                   arg = input(n4+'Nome para o Arquivo :: ')+'.txt'
                   system('touch $(pwd)/%s' %(arg))
                   arq = open(arg, 'w')
                   
                   if (slct) == '1':
                      Ger1(arg, count, arq)
                   if (slct) == '2':
                      Ger2(arg, count, arq)
                   if (slct) == '3':
                      Ger3(arg, count, arq)
                   if (slct) == '4':
                      Ger4(arg, count, arq)
                   if (slct) == '5':
                      Ger5(arg, count, arq)
                   if (slct) == '6':
                      Ger6(arg, count, arq)
                   if (slct) == '7':
                      Ger7(arg, count, arq)
                   if (slct) == '8':
                      Ger8(arg, count, arq)
                   if (slct) == '9':
                      Ger9(arg, count, arq)
               ar(count, slct)
           dig9()
       else:
          nb = input(n5+'[noob] :: ')
 except KeyboardInterrupt:
    print(n1+'\nGoing Out ..\033[m')
    sleep(2)
    exit()
if __name__ == '__main__':
   case()
