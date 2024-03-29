# 싱글 스레드랑 멀티 스레드 비교하기

from myThread import MyThread
from time import ctime, sleep


# 피보나치, 팩토리얼, 합계를 싱글스레드랑 멀티스레드에서 실행시켜 보았다.

def fib(x) :
  sleep(0.005)
  if x<2 : return 1
  return (fib(x-2)+fib(x-1))
  
def fac(x) :
  sleep(0.1)
  if x<2 : return 1
  refutn (x*(fac(x-1))


def sum(x) :
  sleep(0.1)
  if x<2 : return 1
  return (x+sum(x-1))
  


funcs = (fib, fac, sum)
n = 12

def main() :
  nfuncs = range(len(funcs))
  
  print' 싱글스레드'
  for i in nfuncs :
    print ' starting', funcs[i].__name__, 'at : ', ctime()
    print funcs[i](n)
    print funcs[i].__name__, 'finished at :', ctime()
  
  
  print '멀티스레드 '
  threads = []
  for i in nfuncs :
    t = MyThread(funcs[i], (n,), funcs[i].__name__)
    threads.append(t)
  
  
  for i in nfuncs :
    threads[i].start()
  
  
  for i in nfuncs :
    threads[i].join()
    print threads[i].getResult()
  
  
  print 'all DONE'


if __name__ == '__main__' :
  main()
