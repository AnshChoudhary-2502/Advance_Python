import multiprocessing
import concurrent.futures
import requests
def download(url, name):
    print(f"Started downloading File {name}")
    response = requests.get(url)
    open(f"files/File {name}.jpg", "wb").write(response.content)
    print(f"Finished downloading File {name}")

url = "https://picsum.photos/2000/3000"
# p_list = []
# for i in range(50):                 
# #     download(url, i)                # normal task execution
#     p = multiprocessing.Process(target=download, args=[url, i])              # using multiprocessing
#     p.start()
#     p_list.append(p)

# for p in p_list:
#     p.join()

# using ProcessPoolExecutor
n= int(input("No. of images to download:"))
with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(n)]
    l2 = [i for i in range(n)]
    results = executor.map(download, l1, l2)
    for r in results:
        print(r)