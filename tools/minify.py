import re,sys
s=open(sys.argv[1]).read()
if len(sys.argv)>2:
    m=sys.argv[2]
    i=s.index(m); j=s.find('/* ---------- ',i+len(m))
    s=s[i:] if j<0 else s[i:j]
s=re.sub(r'/\*.*?\*/','',s,flags=re.S)
s=re.sub(r'\s+',' ',s)
s=re.sub(r'\s*([{};>])\s*',r'\1',s)
s=re.sub(r',\s+(?=[^)]*(\(|$))',',',s)
s=s.replace(';}','}')
print(s.strip())
