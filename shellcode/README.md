# Shellcode Generator Script

Supports shellcode generation using both sRDI (https://github.com/monoxgas/sRDI) and donut (https://github.com/TheWover/donut).

Will output the generated shellcode in raw, base64 and a \x notated hexstring formats. 

Use donut for .NET assemblies, and sRDI for essentially everything else.


> python3 generator.py -f HelloWorld.dll -m srdi
