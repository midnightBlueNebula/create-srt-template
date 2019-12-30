def createSRTTemplate(vid_h,vid_m,vid_s):
  h = 0
  m = 0
  s = 0
  len = 0
  vid_len = vid_h*60 + vid_m + vid_s/60
  it = 1
  while len < vid_len:
    if (h < 10):
      p_h = "0"+str(h)
    else:  
      p_h = str(h)
    if (m < 10):
      p_m = "0"+str(m)
    else:   
      p_m = str(m)
    if (s < 10): 
      p_s = "0"+str(s)
    else:       
      p_s = str(s)

    print(it)

    if (m < 59 and s < 57):
      if (s+3 < 10):
        print(p_h+":"+p_m+":"+p_s+",500"+" --> " + p_h+":"+p_m+":0"+str(int(p_s)+3)+",000")
      else:
        print(p_h+":"+p_m+":"+p_s+",500"+" --> " + p_h+":"+p_m+":"+str(int(p_s)+3)+",000")
      s += 3
    elif (m < 59 and s>= 57):
      print(p_h+":"+p_m+":"+p_s+",500"+" --> " + p_h+":"+str(int(p_m)+1)+":0"+str(int(p_s)+3-60)+",000")
      m += 1
      s += 3 - 60
    elif (m == 59 and s >= 57):
      print(p_h+":"+p_m+":"+p_s+",500"+" --> " + p_h+":"+"00"+":0"+str(int(p_s)+3-60)+",000")
      h += 1
      m = 0
      s += 3 - 60

    len = h*60 + m + s/60
    it += 1
    print("\n")


createSRTTemplate(0,10,0)
