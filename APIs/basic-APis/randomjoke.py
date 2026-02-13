# https://api.freeapi.app/


# json formatter


# json course of mumshad mannambeth 
import requests 

# def main():
#     response = requests.get('https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1')
#     result = response.json()
#     # print(result['data']['data'][0]['content'])
#     print(result['data']['previousPage'])
#     # print (str(result))
#     # print()




def main():
    response =requests.get('https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech')
    result= response.json()
    print(result['data']['data'][0]['volumeInfo'])


if __name__ == "__main__":
    main()


