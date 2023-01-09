import os 


def main():
    i = 0
    path = "‪C:/Users/mrpie/OneDrive/Documents/Financial Advisors  - AXA Advisors/"
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__maine__':
    main()
    

