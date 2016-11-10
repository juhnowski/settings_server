MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'metro'
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET','PATCH','PUT']

train_schema = {
	'name':{
	'type':'string',
	'minlength':1,
	'maxlength': 10,
	'required': True,
	'unique': True,
	},
	'branch': {
		'type': 'string',
		'minlength': 1,
		'maxlength': 15,
	},
	'arrival': {
		'type': 'datetime',
	},
	'isDebug': {
		'type': 'boolean',
	},
	'A1': {
		'type': 'string',
	},
	'B1': {
		'type': 'string',
	},
	'A2': {
		'type': 'string',
	},
	'B2': {
		'type': 'string',
	},
	'A3': {
		'type': 'string',
	},
	'B3': {
		'type': 'string',
	},
	'A4': {
		'type': 'string',
	},
	'B4': {
		'type': 'string',
	},
	'K1': {
		'type': 'string',
	},
	'K4': {
		'type': 'string',
	},
	'D1': {
		'type': 'string',
	},
	'D4': {
		'type': 'string',
	},
	'Screen3x3_1': {
		'type': 'list',
		'allowed': ["A1","B1","A2","B2","A3","B3","A4","B4","K1","K4","D1","D4"],
	},
	'Screen3x3_2': {
		'type': 'list',
		'allowed': ["A1","B1","A2","B2","A3","B3","A4","B4","K1","K4","D1","D4"],
	},
	'Screen2x3_1': {
		'type': 'list',
		'allowed': ["A1","B1","A2","B2","A3","B3","A4","B4","K1","K4","D1","D4"],
	},
	'Screen2x3_2': {
		'type': 'list',
		'allowed': ["A1","B1","A2","B2","A3","B3","A4","B4","K1","K4","D1","D4"],
	},
	'Screen2x2_1': {
		'type': 'list',
		'allowed': ["A1","B1","A2","B2","A3","B3","A4","B4","K1","K4","D1","D4"],
	},
	'Screen2x2_2': {
		'type': 'list',
		'allowed': ["A1","B1","A2","B2","A3","B3","A4","B4","K1","K4","D1","D4"],
	},
	'Screen2x2_3': {
		'type': 'list',
		'allowed': ["A1","B1","A2","B2","A3","B3","A4","B4","K1","K4","D1","D4"],
	},
	'brightness': {
		'type': 'integer',
	},
	'contrast': {
		'type': 'integer',
	},
	'shift_x': {
		'type': 'integer',
	},
	'shift_y': {
		'type': 'integer',
	},
	'compress_x': {
		'type': 'integer',
	},
	'compress_y': {
		'type': 'integer',
	},
	'KEY_F1': {
		'type': 'integer',
	},
	'KEY_F2': {
		'type': 'integer',
	},
	'KEY_F3': {
		'type': 'integer',
	},
	'KEY_F4': {
		'type': 'integer',
	},
	'KEY_F5': {
		'type': 'integer',
	},
	'KEY_F6': {
		'type': 'integer',
	},
	'KEY_F12': {
		'type': 'integer',
	},
	'KEY_Num0': {
		'type': 'integer',
	},
	'KEY_Num1': {
		'type': 'integer',
	},
	'KEY_Num2': {
		'type': 'integer',
	},
	'KEY_Num3': {
		'type': 'integer',
	},
	'KEY_Num4': {
		'type': 'integer',
	},
	'KEY_Num5': {
		'type': 'integer',
	},
	'KEY_Num6': {
		'type': 'integer',
	},
	'KEY_Num7': {
		'type': 'integer',
	},
	'KEY_Num8': {
		'type': 'integer',
	},
	'KEY_Num9': {
		'type': 'integer',
	},
	'KEY_ENTER': {
		'type': 'integer',
	},
	'KEY_ESC': {
		'type': 'integer',
	},
	'id_can': {
		'type': 'list',
		'allowed': ["nothing","IRMA"],
	},
	'rs_485_1': {
		'type': 'list',
		'allowed': ["nothing","ORBITA","ISKRA","OMNICOM"],
	},
	'rs_485_2': {
		'type': 'list',
		'allowed': ["nothing","ORBITA","ISKRA","OMNICOM"],
	},
	'rs_232_1': {
		'type': 'list',
		'allowed': ["nothing","in GNSS","out GNSS"],
	},
	'rs_232_2': {
		'type': 'list',
		'allowed': ["nothing","in GNSS","out GNSS"],
	},
	'videoreg': {
		'type': 'dict',
		'schema': {
			'id': {'type': 'integer'},
			'alias': {'type': 'string'},
			'channels': {'type': 'integer'},
		}
	},
	'disk': {
		'type': 'dict',
		'schema': {
			'id': {'type': 'integer'},
			'disk_type': {'type':'list', 'allowed': ["HDD","SD","FLASH"],},
			'disk_free': {'type': 'integer'},
			'disk_total': {'type': 'integer'},
		}
	},
	'date_format': {
		'type': 'list',
		'allowed': ["MM/DD/YY","YY/MM/DD","DD/MM/YY"],
	},
	'time_format': {
		'type': 'list',
		'allowed': ["12","24"],
	},
	'time_zone': {
		'type': 'list',
		'allowed':["−12","−11","−10","−9:30","−9","−8:30","−8","−7","−6","−5","−4:30","−4","−3:30","−3","−2:30","−2","−1","−0:44","−0:25","0","+0:20","+0:30","+1","+2","+3","+3:30","+4","+4:30","+4:51","+5","+5:30","+5:40","+5:45","+6","+6:30","+7","+7:20","+7:30","+8","+8:30","+8:45","+9","+9:30","+10","+10:30","+11","+11:30","+12","+12:45","+13","+13:45","+14"],
	},
	'time_sync': {
		'type': 'list',
		'allowed':["GNSS","VIDEOSERVER","SYNC"],
	},
	'sync_on': {
		'type': 'boolean',
	},
	'add_hours': {
		'type':	'list',
		'allowed':["1","2"],
	},
	'mode': {
		'type':	'list',
		'allowed':["week","month"],
	},
	'from_month': {
		'type':	'list',
		'allowed':["Jan","Feb","Mar","Apr","May","Jun"],
	},
	'from_week': {
		'type':	'list',
		'allowed':["1","2","3","4","last"],		
	},
	'from_day_week': {
		'type':	'list',
		'allowed':["Su","Mo","Tu","We","Th","Fr","Sa"],		
	},
	'from_time': {
		'type':'string',
	},
	'to_month': {
		'type':	'list',
		'allowed':["Jan","Feb","Mar","Apr","May","Jun"],
	},
	'to_week': {
		'type':	'list',
		'allowed':["1","2","3","4","last"],		
	},
	'to_day_week': {
		'type':	'list',
		'allowed':["Su","Mo","Tu","We","Th","Fr","Sa"],		
	},
	'to_time': {
		'type':'string',
	},	'dhcp': {
		'type':'boolean',
	},
	'static_ip': {
		'type':'boolean',
	},
	'ip': {
		'type':'string',
	},
	'mask': {
		'type':'string',
	},
	'gw': {
		'type':'string',
	},
	'dns_1': {
		'type':'string',
	},
	'dns_2': {
		'type':'string',
	},		
	'videoserver': {
		'type': 'dict',
		'schema': {
			'id': {'type': 'integer'},
			'name': {'type': 'string'},
			'active': {'type': 'boolean'},
			'ip': {'type': 'string'},
			'port': {'type': 'integer'},
			'protocol': {'type': 'list', 'allowed':["tcp","udp","rtsp"]},
		}
	},
	'media_service':{
		'type': 'dict',
		'schema': {
			'id': {'type': 'integer'},
			'server_id': {'type': 'integer'},
			'name': {'type': 'string'},
			'active': {'type': 'boolean'},
			'ip': {'type': 'string'},
			'port': {'type': 'integer'},
			'protocol': {'type': 'list', 'allowed':["tcp","udp","rtsp"]},
		}
	},
	'ip_camera': {
		'type': 'dict',
		'schema': {
			'id': {'type': 'integer'},
			'name': {'type': 'string'},
			'active': {'type': 'boolean'},
			'ip': {'type': 'string'},
			'port': {'type': 'integer'},
			'substreams': {'type': 'integer'},
			'protocol': {'type': 'list', 'allowed':["tcp","udp","rtsp"]},
		}
	},
	'script': {
		'type': 'string',
	},
	'script_done': {
		'type': 'boolean',
	},
	'status': {
		'type': 'string',
	},
	'csv': {
		'type': 'string',
	},
}

train = {
	'item_title':'train',
	'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': train_schema,
	'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
}

DOMAIN = {'train':train,}
