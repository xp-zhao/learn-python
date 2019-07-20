import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
result = requests.get(url)
print("Status code: ", result.status_code)

# 存储 api 响应结果
response_dict = result.json()

# 处理结果
print(response_dict.keys())

print("Total repositories: ", response_dict['total_count'])
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)