part of code was omitted  <br />
failed to make it on time since didn't figure out how to deal with request (requests only accept path to file as certificate value in query)
<br /> <br /> 
After some googling I didn't found reasonable way to do it except patching requests library itself, which is I dunno if it's something I should do. <br />
Other solution was to make temporary files and use certificate and key this way but after asking they confirmed that I must not use them as files at all.

Create a Django project, with which using jsonrpc-2.0 (endpoint: https://**) you can call a remote api method using the attached certificate + key pair for authorization ("two-way TLS") <br />
For example, the jsonrpc-2.0 method "auth.check" is called. <br />
The content (!) Of the certificate and key is written somewhere in one of the project files (for example, in settings.py) as text variables (not as paths to files).  <br />
Use only python standard library (besides django) for the whole project. <br />
Django part: primitive UI one page: one html form (method name + submit + possibly method parameters) + displaying the result. <br />
The api call method should be like reusable code to call any jsonrpc method at any endpoint with primitive error handling etc. (as a s eparate module or as a separate django app) <br />
