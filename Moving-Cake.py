#Recursive function
def CakeLayers(n , source="Silver", dest="Golden", temp="Bronze"):

    if n == 1:
    #moves final remaining layer from source to dest
        print ("Move layer 1 from plate",source,"to plate",dest)
        return 
        
    #moves layer from source to temp using dest
    CakeLayers(n-1, source, temp, dest)
    
    #moves layer from source to dest directly
    print ("Move layer",n,"from plate",source,"to plate",dest)
    
    #moves layer from temp to dest using source
    CakeLayers(n-1, temp, dest, source)
   
#Main Call
CakeLayers (int(input('Enter the no of stories:\n')))
