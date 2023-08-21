import requests
class Client():
	def __init__(self):
		self.api="https://check-host.net"
		self.headers={"user-agent":"okhttp/3.12.1","Accept":"application/json"}
	def check_tcp(self,host:str,max_nodes:str):
		return requests.get(f"{self.api}/check-tcp?host={host}&max_nodes={max_nodes}",headers=self.headers).json()
	def check_ping(self,host:str,max_nodes:str):
		return requests.get(f"{self.api}/check-ping?host={host}&max_nodes={max_nodes}",headers=self.headers).json()
	def check_http(self,host:str,max_nodes:str):
		return requests.get(f"{self.api}/check-http?host={host}&max_nodes={max_nodes}",headers=self.headers).json()
	def check_dns(self,host:str,max_nodes:str):
		return requests.get(f"{self.api}/check-dns?host={host}&max_nodes={max_nodes}",headers=self.headers).json()
	def nodes_hosts(self):
		return requests.get(f"{self.api}/nodes/hosts",headers=self.headers).json()
	def check_result(self,request_id:str):
		return requests.get(f"{self.api}/check-result/{request_id}",headers=self.headers).json()