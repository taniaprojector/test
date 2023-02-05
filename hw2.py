
v1 = property_transfer_xml = """
<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';
//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';
//urn:multiCall/sessionId['?']</con:targetPath>
"""#просто ввела змінну v1 з повним великим значенням

result = v1.split('<con:targetType>'); #це поділ на 2 елементи за назвою тега
print(result[1]); # це вивести другий елемент масива, памятаємо, що рахунок завжди 
print(result[0][:7]); # вивести перші 7 символів другого елемента масива, що і є нашою відповіддю
fin_result = result[0][:7];
print('Result of the second HW is -' + fin_result); 
