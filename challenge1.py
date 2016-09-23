a=raw_input("string :")
st=''
#l1=list(a.split(" "))
#global e,w,q
#for j in l1:
if '' in a:
    st=st+""
   
for i in a:
    if i=="k":
        st=st+a.replace('k','m')
        
    elif i=="o":
        st=st+a.replace('o','q')
            
    elif i=="e":
        st=st+a.replace('e','g')

    else:
        st=st+chr(ord(i)+2)
    
print st
#print b+e+w+q

