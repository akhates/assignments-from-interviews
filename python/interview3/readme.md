part of code was omitted  <br />
failed to make it on time since didn't figure out how to deal with request (requests only accept path to file as certificate value in query)
<br /> <br /> 
After some googling I didn't found reasonable way to do it except patching requests library itself, which is I dunno if it's something I should do. <br />
Other solution was to make temporary files and use certificate and key this way but after asking they confirmed that I must not use them as files at all.

Create a Django project, using jsonrpc-2.0 (endpoint: https://**) call a remote api method "auth.check" using the attached certificate + key pair for authorization ("two-way TLS") <br />
The content (!) Of the certificate and key must be written somewhere in one of the project files (for example in settings.py) as text variables (not as paths to files).  <br />
Use can only use standard python library (besides django) for the whole project. <br />
Django part: primitive UI, on page: one html form (method name + submit + possibly method parameters) + displaying the result. <br />
The api method call should be an reusable code that can be used to call any jsonrpc method at any endpoint with primitive error handling and etc. (as a separate module or as a separate django app) <br />
