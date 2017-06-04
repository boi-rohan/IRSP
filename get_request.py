import requests

def get_req(url, court_pk, date):
	# date entry example: 2017-09-22 (string) {yyyy-mm-dd}
	# url example: 'https://abc.acb.com/' (string)
	# court_pk - int
	data = (requests.get(url + 'api/post_datetimevalue/')).json()
	final_list = []
	for item in data:
		if item['court']==court_pk and item['date_time'][0:10].encode('ascii', 'replace')==date:
			final_list.append([item['date_time'].encode('ascii', 'replace'), item['value']])

	return final_list
