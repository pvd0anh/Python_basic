# File2.py  
    
print("File2 __name__ = %s" %__name__) 
    
if __name__ == "__main__":  
    print("File2 đang được chạy") 
else:  
    print("File2 đã được import") 

'''Output:

File1 __name__ = File1
File1 is being imported
File2 __name__ = __main__
File2 is being run directly'''