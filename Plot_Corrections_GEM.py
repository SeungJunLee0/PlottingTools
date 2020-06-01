from geometryDiffVisualization import *
import os,sys
for endcap in 1,2:
#  for disk in 1,2,3,4:
  disk = 1
  if endcap == 1: diskPrettyName = "__GEp%s" % disk
  else:           diskPrettyName = "__GEm%s" % disk
  imageName = alignmentName+"-"+referenceName+diskPrettyName
  svgName = imageName+".svg"
  draw_disk(g1, g_ref, endcap, disk, svgPath+svgName, length_factor, angle_factor)
  pngName = imageName+".png"
  orderpng = "rsvg-convert ./RESULT/"+alignmentName+"/SVG/"+svgName + " > ./RESULT/" + alignmentName + "/PNG/"+pngName

  os.system(orderpng)
  retvalue = os.system("convert -density 104.2 %s %s" % (svgPath+svgName, pngPath+pngName) )

if isReport:
  for r1 in report1:
    if ( r1.postal_address[0] == "GEM" and r1.status == "PASS" and r1.postal_address[3] != 4 ) :
      endcap  = r1.postal_address[1]
      disk    = r1.postal_address[2]
      ring    = r1.postal_address[3]
      chamber = r1.postal_address[4]
      dx_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].x - g_ref.gem[endcap, disk, ring, chamber].x)*signConventions["GEM", endcap, disk, ring, chamber][0]
      h_dx.Fill(dx_mm)
      ex_mm = 10.*r1.deltax.error
      h_ex.Fill(ex_mm)
      if ex_mm != 0.0: h_px.Fill(dx_mm/ex_mm)
      dy_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].y - g_ref.gem[endcap, disk, ring, chamber].y)*signConventions["GEM", endcap, disk, ring, chamber][1]
      h_dy.Fill(dy_mm)
      ey_mm = 10.*r1.deltay.error
      h_ey.Fill(ey_mm)
      if ey_mm != 0.0: h_py.Fill(dy_mm/ey_mm)
      dz_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].z - g_ref.gem[endcap, disk, ring, chamber].z)*signConventions["GEM", endcap, disk, ring, chamber][2]
      h_dz.Fill(dz_mm)
      ez_mm = 10.*r1.deltaz.error
      h_ez.Fill(ez_mm)
      if ez_mm != 0.0: h_pz.Fill(dz_mm/ez_mm)
      dphix_mrad = 1000.0*(g1.gem[endcap, disk, ring, chamber].phix - g_ref.gem[endcap, disk, ring, chamber].phix)
      h_dphix.Fill(dphix_mrad)
      ephix_mrad = 1000.*r1.deltaphix.error
      h_ephix.Fill(ephix_mrad)
      if ephix_mrad != 0.0: h_pphix.Fill(dphix_mrad/ephix_mrad)
      dphiy_mrad = 1000.0*(g1.gem[endcap, disk, ring, chamber].phiy - g_ref.gem[endcap, disk, ring, chamber].phiy)
      h_dphiy.Fill(dphiy_mrad)
      ephiy_mrad = 1000.*r1.deltaphiy.error
      h_ephiy.Fill(ephiy_mrad)
      if ephiy_mrad != 0.0: h_pphiy.Fill(dphiy_mrad/ephiy_mrad)
      dphiz_mrad = 1000.0*(g1.gem[endcap, disk, ring, chamber].phiz - g_ref.gem[endcap, disk, ring, chamber].phiz)
      h_dphiz.Fill(dphiz_mrad)
      ephiz_mrad = 1000.*r1.deltaphiz.error
      h_ephiz.Fill(ephiz_mrad)
      if ephiz_mrad != 0.0: h_pphiz.Fill(dphiz_mrad/ephiz_mrad)
else:
  for endcap in 1,2:
#  for disk in 1, 2, 3, 4:
    disk = 1
#    if disk == 1: rings = 1
    ring = 1
# 	else:         rings = 1,2
#for ring in rings:
#if disk != 1 and ring == 1: chambers = range(1,18+1)
#else:                       chambers = range(1,36+1)
    chambers = range(1,36+1)
    for chamber in chambers:
      dx_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].x - g_ref.gem[endcap, disk, ring, chamber].x)*signConventions["GEM", endcap, disk, ring, chamber][0]
      h_dx.Fill(dx_mm)
      dy_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].y - g_ref.gem[endcap, disk, ring, chamber].y)*signConventions["GEM", endcap, disk, ring, chamber][1]
      h_dy.Fill(dy_mm)
      dz_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].z - g_ref.gem[endcap, disk, ring, chamber].z)*signConventions["GEM", endcap, disk, ring, chamber][2]
      h_dz.Fill(dz_mm)
      dphix_mrad = 1000.0*(g1.gem[endcap, disk, ring, chamber].phix - g_ref.gem[endcap, disk, ring, chamber].phix)
      h_dphix.Fill(dphix_mrad)
      dphiy_mrad = 1000.0*(g1.gem[endcap, disk, ring, chamber].phiy - g_ref.gem[endcap, disk, ring, chamber].phiy)
      h_dphiy.Fill(dphiy_mrad)
      dphiz_mrad = 1000.0*(g1.gem[endcap, disk, ring, chamber].phiz - g_ref.gem[endcap, disk, ring, chamber].phiz)
      h_dphiz.Fill(dphiz_mrad)

#*******************************************************************************

systemPrettyName = "GE ALL"
histTitle = systemPrettyName+": "+correctionName
littleLabel = alignmentName+" - "+referenceName

h_dx.SetTitle(histTitle)
fit = FitAndDraw(h_dx, littleLabel, 0)
legend.Draw()
pngName = "GEM_dx.png"
pdfName = "GEM_dx.pdf"
c1.SaveAs(pngPath+pngName)
c1.SaveAs(pdfPath+pdfName)

h_dy.SetTitle(histTitle)
fit = FitAndDraw(h_dy, littleLabel, 0)
legend.Draw()
pngName = "GEM_dy.png"
pdfName = "GEM_dy.pdf"
c1.SaveAs(pngPath+pngName)
c1.SaveAs(pdfPath+pdfName)

h_dz.SetTitle(histTitle)
fit = FitAndDraw(h_dz, littleLabel, 0)
legend.Draw()
pngName = "GEM_dz.png"
pdfName = "GEM_dz.pdf"
c1.SaveAs(pngPath+pngName)
c1.SaveAs(pdfPath+pdfName)

h_dphix.SetTitle(histTitle)
fit = FitAndDraw(h_dphix, littleLabel, 0)
legend.Draw()
pngName = "GEM_dphix.png"
pdfName = "GEM_dphix.pdf"
c1.SaveAs(pngPath+pngName)
c1.SaveAs(pdfPath+pdfName)

h_dphiy.SetTitle(histTitle)
fit = FitAndDraw(h_dphiy, littleLabel, 0)
legend.Draw()
pngName = "GEM_dphiy.png"
pdfName = "GEM_dphiy.pdf"
c1.SaveAs(pngPath+pngName)
c1.SaveAs(pdfPath+pdfName)

h_dphiz.SetTitle(histTitle)
fit = FitAndDraw(h_dphiz, littleLabel, 0)
legend.Draw()
pngName = "GEM_dphiz.png"
pdfName = "GEM_dphiz.pdf"
c1.SaveAs(pngPath+pngName)
c1.SaveAs(pdfPath+pdfName)

#*******************************************************************************

if isReport:
  histTitle = systemPrettyName+": Alignment fit uncertainties"
  
  h_ex.SetTitle(histTitle)
  fit = FitAndDraw(h_ex, alignmentName, 0)
  legend.Draw()
  pngName = "GEM_ex.png"
  pdfName = "GEM_ex.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_ey.SetTitle(histTitle)
  fit = FitAndDraw(h_ey, alignmentName, 0)
  legend.Draw()
  pngName = "GEM_ey.png"
  pdfName = "GEM_ey.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_ez.SetTitle(histTitle)
  fit = FitAndDraw(h_ez, alignmentName, 0)
  legend.Draw()
  pngName = "GEM_ez.png"
  pdfName = "GEM_ez.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_ephix.SetTitle(histTitle)
  fit = FitAndDraw(h_ephix, alignmentName, 0)
  legend.Draw()
  pngName = "GEM_ephix.png"
  pdfName = "GEM_ephix.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_ephiy.SetTitle(histTitle)
  fit = FitAndDraw(h_ephiy, alignmentName, 0)
  legend.Draw()
  pngName = "GEM_ephiy.png"
  pdfName = "GEM_ephiy.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_ephiz.SetTitle(histTitle)
  fit = FitAndDraw(h_ephiz, alignmentName, 0)
  legend.Draw()
  pngName = "GEM_ephiz.png"
  pdfName = "GEM_ephiz.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)

  #*******************************************************************************

  histTitle = systemPrettyName+": Pulls"
  
  h_px.SetTitle(histTitle)
  fit = FitAndDraw(h_px, littleLabel, 1)
  legend.Draw()
  pngName = "GEM_px.png"
  pdfName = "GEM_px.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_py.SetTitle(histTitle)
  fit = FitAndDraw(h_py, littleLabel, 1)
  legend.Draw()
  pngName = "GEM_py.png"
  pdfName = "GEM_py.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_pz.SetTitle(histTitle)
  fit = FitAndDraw(h_pz, littleLabel, 1)
  legend.Draw()
  pngName = "GEM_pz.png"
  pdfName = "GEM_pz.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_pphix.SetTitle(histTitle)
  fit = FitAndDraw(h_pphix, littleLabel, 1)
  legend.Draw()
  pngName = "GEM_pphix.png"
  pdfName = "GEM_pphix.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_pphiy.SetTitle(histTitle)
  fit = FitAndDraw(h_pphiy, littleLabel, 1)
  legend.Draw()
  pngName = "GEM_pphiy.png"
  pdfName = "GEM_pphiy.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  
  h_pphiz.SetTitle(histTitle)
  fit = FitAndDraw(h_pphiz, littleLabel, 1)
  legend.Draw()
  pngName = "GEM_pphiz.png"
  pdfName = "GEM_pphiz.pdf"
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)

#*******************************************************************************

gemGroupTable = GemGroupTable()

gemGroupTable.AddGemGroupVar("dxRMS",         "&delta;x (mm) <br>RMS",                           "$RMS(\\delta x)$",                     "mm")
gemGroupTable.AddGemGroupVar("dxGaussSig",    "&delta;x (mm) <br>Gauss Sigma",                   "$\\sigma_{Gauss}(\\delta x)$",         "mm")
gemGroupTable.AddGemGroupVar("dyRMS",         "&delta;y (mm) <br>RMS",                           "$RMS(\\delta y)$",                     "mm")
gemGroupTable.AddGemGroupVar("dyGaussSig",    "&delta;y (mm) <br>Gauss Sigma",                   "$\\sigma_{Gauss}(\\delta y)$",         "mm")
gemGroupTable.AddGemGroupVar("dzRMS",         "&delta;z (mm) <br>RMS",                           "$RMS(\\delta z)$",                     "mm")
gemGroupTable.AddGemGroupVar("dzGaussSig",    "&delta;z (mm) <br>Gauss Sigma",                   "$\\sigma_{Gauss}(\\delta z)$",         "mm")
gemGroupTable.AddGemGroupVar("dphixRMS",      "&delta;&phi;<sub>x</sub> (mrad) <br>RMS",         "$RMS(\\delta \\phi_{x})$",             "mrad")
gemGroupTable.AddGemGroupVar("dphixGaussSig", "&delta;&phi;<sub>x</sub> (mrad) <br>Gauss Sigma", "$\\sigma_{Gauss}(\\delta \\phi_{x})$", "mrad")
gemGroupTable.AddGemGroupVar("dphiyRMS",      "&delta;&phi;<sub>y</sub> (mrad) <br>RMS",         "$RMS(\\delta \\phi_{y})$",             "mrad")
gemGroupTable.AddGemGroupVar("dphiyGaussSig", "&delta;&phi;<sub>y</sub> (mrad) <br>Gauss Sigma", "$\\sigma_{Gauss}(\\delta \\phi_{y})$", "mrad")
gemGroupTable.AddGemGroupVar("dphizRMS",      "&delta;&phi;<sub>z</sub> (mrad) <br>RMS",         "$RMS(\\delta \\phi_{z})$",             "mrad")
gemGroupTable.AddGemGroupVar("dphizGaussSig", "&delta;&phi;<sub>z</sub> (mrad) <br>Gauss Sigma", "$\\sigma_{Gauss}(\\delta \\phi_{z})$", "mrad")

gemGroupTable.AddGemGroupVar("exMean",         "&sigma;<sub>fit</sub>x (mm) <br>Mean",                         "$Mean(\\sigma_{fit} x) $",               "mm")
gemGroupTable.AddGemGroupVar("exGaussMean",    "&sigma;<sub>fit</sub>x (mm) <br>Gauss Mean",                   "$Mean_{Gauss}(\\sigma_{fit} x) $",       "mm")
gemGroupTable.AddGemGroupVar("eyMean",         "&sigma;<sub>fit</sub>y (mm) <br>Mean",                         "$Mean(\\sigma_{fit} y) $",               "mm")
gemGroupTable.AddGemGroupVar("eyGaussMean",    "&sigma;<sub>fit</sub>y (mm) <br>Gauss Mean",                   "$Mean_{Gauss}(\\sigma_{fit} y) $",       "mm")
gemGroupTable.AddGemGroupVar("ezMean",         "&sigma;<sub>fit</sub>z (mm) <br>Mean",                         "$Mean(\\sigma_{fit} z) $",               "mm")
gemGroupTable.AddGemGroupVar("ezGaussMean",    "&sigma;<sub>fit</sub>z (mm) <br>Gauss Mean",                   "$Mean_{Gauss}(\\sigma_{fit} z) $",       "mm")
gemGroupTable.AddGemGroupVar("ephixMean",      "&sigma;<sub>fit</sub>&phi;<sub>x</sub> (mrad) <br>Mean",       "$Mean(\\sigma_{fit} \\phi_x) $",         "mrad")
gemGroupTable.AddGemGroupVar("ephixGaussMean", "&sigma;<sub>fit</sub>&phi;<sub>x</sub> (mrad) <br>Gauss Mean", "$Mean_{Gauss}(\\sigma_{fit} \\phi_x) $", "mrad")
gemGroupTable.AddGemGroupVar("ephiyMean",      "&sigma;<sub>fit</sub>&phi;<sub>y</sub> (mrad) <br>Mean",       "$Mean(\\sigma_{fit} \\phi_y) $",         "mrad")
gemGroupTable.AddGemGroupVar("ephiyGaussMean", "&sigma;<sub>fit</sub>&phi;<sub>y</sub> (mrad) <br>Gauss Mean", "$Mean_{Gauss}(\\sigma_{fit} \\phi_y) $", "mrad")
gemGroupTable.AddGemGroupVar("ephizMean",      "&sigma;<sub>fit</sub>&phi;<sub>z</sub> (mrad) <br>Mean",       "$Mean(\\sigma_{fit} \\phi_z) $",         "mrad")
gemGroupTable.AddGemGroupVar("ephizGaussMean", "&sigma;<sub>fit</sub>&phi;<sub>z</sub> (mrad) <br>Gauss Mean", "$Mean_{Gauss}(\\sigma_{fit} \\phi_z) $", "mrad")

gemGroupTable.AddGemGroupVar("pxRMS","x pull <br>RMS",                                 "$RMS(P x)$",                     None)
gemGroupTable.AddGemGroupVar("pxGaussSig","x pull <br>Gauss Sigma",                    "$\\sigma_{Gauss}(P x)$",         None)
gemGroupTable.AddGemGroupVar("pyRMS","y pull <br>RMS",                                 "$RMS(P y)$",                     None)
gemGroupTable.AddGemGroupVar("pyGaussSig","y pull <br>Gauss Sigma",                    "$\\sigma_{Gauss}(P y)$",         None)
gemGroupTable.AddGemGroupVar("pzRMS","z pull <br>RMS",                                 "$RMS(P z)$",                     None)
gemGroupTable.AddGemGroupVar("pzGaussSig","z pull <br>Gauss Sigma",                    "$\\sigma_{Gauss}(P z)$",         None)
gemGroupTable.AddGemGroupVar("pphixRMS","&phi;<sub>x</sub> pull <br>RMS",              "$RMS(P \\phi_{x})$",             None)
gemGroupTable.AddGemGroupVar("pphixGaussSig","&phi;<sub>x</sub> pull <br>Gauss Sigma", "$\\sigma_{Gauss}(P \\phi_{x})$", None)
gemGroupTable.AddGemGroupVar("pphiyRMS","&phi;<sub>y</sub> pull <br>RMS",              "$RMS(P \\phi_{y})$",             None)
gemGroupTable.AddGemGroupVar("pphiyGaussSig","&phi;<sub>y</sub> pull <br>Gauss Sigma", "$\\sigma_{Gauss}(P \\phi_{y})$", None)
gemGroupTable.AddGemGroupVar("pphizRMS","&phi;<sub>z</sub> pull <br>RMS",              "$RMS(P \\phi_{z})$",             None)
gemGroupTable.AddGemGroupVar("pphizGaussSig","&phi;<sub>z</sub> pull <br>Gauss Sigma", "$\\sigma_{Gauss}(P \\phi_{z})$", None)

gemTab_dx    = GemTable()
gemTab_dy    = GemTable()
gemTab_dz    = GemTable()
gemTab_dphix = GemTable()
gemTab_dphiy = GemTable()
gemTab_dphiz = GemTable()

gemTab_ex    = GemTable()
gemTab_ey    = GemTable()
gemTab_ez    = GemTable()
gemTab_ephix = GemTable()
gemTab_ephiy = GemTable()
gemTab_ephiz = GemTable()

gemTab_px    = GemTable()
gemTab_py    = GemTable()
gemTab_pz    = GemTable()
gemTab_pphix = GemTable()
gemTab_pphiy = GemTable()
gemTab_pphiz = GemTable()

for endcap in 1,2:
# for disk in 1, 2, 3, 4:
  disk = 1 
#if disk == 1: rings = 1,2,3
#    else:         rings = 1,2
  ring = 1 
#for ring in rings:
  h_dx.Reset("ICESM")
  h_dy.Reset("ICESM")
  h_dz.Reset("ICESM")
  h_dphix.Reset("ICESM")
  h_dphiy.Reset("ICESM")
  h_dphiz.Reset("ICESM")
  h_ex.Reset("ICESM")
  h_ey.Reset("ICESM")
  h_ez.Reset("ICESM")
  h_ephix.Reset("ICESM")
  h_ephiy.Reset("ICESM")
  h_ephiz.Reset("ICESM")
  h_px.Reset("ICESM")
  h_py.Reset("ICESM")
  h_pz.Reset("ICESM")
  h_pphix.Reset("ICESM")
  h_pphiy.Reset("ICESM")
  h_pphiz.Reset("ICESM")
  
  if isReport:
    for r1 in report1:
      if ( r1.postal_address[0] == "GEM" and r1.status == "PASS" and r1.postal_address[1] == endcap and r1.postal_address[2] == disk and r1.postal_address[3] == ring ) :
        chamber  = r1.postal_address[4]
        dx_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].x - g_ref.gem[endcap, disk, ring, chamber].x)*signConventions["GEM", endcap, disk, ring, chamber][0]
        h_dx.Fill(dx_mm)
        gemTab_dx.FillGem(endcap, disk, ring, chamber,"%.3f" % dx_mm)
        ex_mm = 10.*r1.deltax.error
        h_ex.Fill(ex_mm)
        gemTab_ex.FillGem(endcap, disk, ring, chamber,"%.3f" % ex_mm)
        if ex_mm != 0.0:
          px = dx_mm/ex_mm
          h_px.Fill(px)
          gemTab_px.FillGem(endcap, disk, ring, chamber,"%.3f" % px)
        dy_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].y - g_ref.gem[endcap, disk, ring, chamber].y)*signConventions["GEM", endcap, disk, ring, chamber][1]
        h_dy.Fill(dy_mm)
        gemTab_dy.FillGem(endcap, disk, ring, chamber,"%.3f" % dy_mm)
        ey_mm = 10.*r1.deltay.error
        h_ey.Fill(ey_mm)
        gemTab_ey.FillGem(endcap, disk, ring, chamber,"%.3f" % ey_mm)
        if ey_mm != 0.0:
          py = dy_mm/ey_mm
          h_py.Fill(py)
          gemTab_py.FillGem(endcap, disk, ring, chamber,"%.3f" % py)
        dz_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].z - g_ref.gem[endcap, disk, ring, chamber].z)*signConventions["GEM", endcap, disk, ring, chamber][2]
        h_dz.Fill(dz_mm)
        gemTab_dz.FillGem(endcap, disk, ring, chamber,"%.3f" % dz_mm)
        ez_mm = 10.*r1.deltaz.error
        h_ez.Fill(ez_mm)
        gemTab_ez.FillGem(endcap, disk, ring, chamber,"%.3f" % ez_mm)
        if ez_mm != 0.0:
          pz = dz_mm/ez_mm
          h_pz.Fill(pz)
          gemTab_pz.FillGem(endcap, disk, ring, chamber,"%.3f" % pz)
        dphix_mrad = 1000.*(g1.gem[endcap, disk, ring, chamber].phix - g_ref.gem[endcap, disk, ring, chamber].phix)
        h_dphix.Fill(dphix_mrad)
        gemTab_dphix.FillGem(endcap, disk, ring, chamber,"%.3f" % dphix_mrad)
        ephix_mrad = 1000.*r1.deltaphix.error
        h_ephix.Fill(ephix_mrad)
        gemTab_ephix.FillGem(endcap, disk, ring, chamber,"%.3f" % ephix_mrad)
        if ephix_mrad != 0.0:
          pphix = dphix_mrad/ephix_mrad
          h_pphix.Fill(pphix)
          gemTab_pphix.FillGem(endcap, disk, ring, chamber,"%.3f" % pphix)
        dphiy_mrad = 1000.*(g1.gem[endcap, disk, ring, chamber].phiy - g_ref.gem[endcap, disk, ring, chamber].phiy)
        h_dphiy.Fill(dphiy_mrad)
        gemTab_dphiy.FillGem(endcap, disk, ring, chamber,"%.3f" % dphiy_mrad)
        ephiy_mrad = 1000.*r1.deltaphiy.error
        h_ephiy.Fill(ephiy_mrad)
        gemTab_ephiy.FillGem(endcap, disk, ring, chamber,"%.3f" % ephiy_mrad)
        if ephiy_mrad != 0.0:
          pphiy = dphiy_mrad/ephiy_mrad
          h_pphiy.Fill(pphiy)
          gemTab_pphiy.FillGem(endcap, disk, ring, chamber,"%.3f" % pphiy)
        dphiz_mrad = 1000.*(g1.gem[endcap, disk, ring, chamber].phiz - g_ref.gem[endcap, disk, ring, chamber].phiz)
        h_dphiz.Fill(dphiz_mrad)
        gemTab_dphiz.FillGem(endcap, disk, ring, chamber,"%.3f" % dphiz_mrad)
        ephiz_mrad = 1000.*r1.deltaphiz.error
        h_ephiz.Fill(ephiz_mrad)
        gemTab_ephiz.FillGem(endcap, disk, ring, chamber,"%.3f" % ephiz_mrad)
        if ephiz_mrad != 0.0:
          pphiz = dphiz_mrad/ephiz_mrad
          h_pphiz.Fill(pphiz)
          gemTab_pphiz.FillGem(endcap, disk, ring, chamber,"%.3f" % pphiz)

  else: # if isReport
    if disk != 1 and ring == 1: chambers = range(1,18+1)
    else:                       chambers = range(1,36+1)
    for chamber in chambers:
      dx_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].x - g_ref.gem[endcap, disk, ring, chamber].x)*signConventions["GEM", endcap, disk, ring, chamber][0]
      h_dx.Fill(dx_mm)
      gemTab_dx.FillGem(endcap, disk, ring, chamber,"%.3f" % dx_mm)
      dy_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].y - g_ref.gem[endcap, disk, ring, chamber].y)*signConventions["GEM", endcap, disk, ring, chamber][1]
      h_dy.Fill(dy_mm)
      gemTab_dy.FillGem(endcap, disk, ring, chamber,"%.3f" % dy_mm)
      dz_mm = 10.0*(g1.gem[endcap, disk, ring, chamber].z - g_ref.gem[endcap, disk, ring, chamber].z)*signConventions["GEM", endcap, disk, ring, chamber][2]
      h_dz.Fill(dz_mm)
      gemTab_dz.FillGem(endcap, disk, ring, chamber,"%.3f" % dz_mm)
      dphix_mrad = 1000.0*(g1.gem[endcap, disk, ring, chamber].phix - g_ref.gem[endcap, disk, ring, chamber].phix)
      h_dphix.Fill(dphix_mrad)
      gemTab_dphix.FillGem(endcap, disk, ring, chamber,"%.3f" % dphix_mrad)
      dphiy_mrad = 1000.0*(g1.gem[endcap, disk, ring, chamber].phiy - g_ref.gem[endcap, disk, ring, chamber].phiy)
      h_dphiy.Fill(dphiy_mrad)
      gemTab_dphiy.FillGem(endcap, disk, ring, chamber,"%.3f" % dphiy_mrad)
      dphiz_mrad = 1000.0*(g1.gem[endcap, disk, ring, chamber].phiz - g_ref.gem[endcap, disk, ring, chamber].phiz)
      h_dphiz.Fill(dphiz_mrad)
      gemTab_dphiz.FillGem(endcap, disk, ring, chamber,"%.3f" % dphiz_mrad)

#** Corrections: save plots and fill tables over homogeneous chambers ******
      
  if endcap == 1:
    sEndcapSign = "+"
    sEndcapPorM = "p"
  else:
    sEndcapSign = "-"
    sEndcapPorM = "m"
  gemGroupPrettyName = "GE" + sEndcapSign + ("%s/%s/ALL" % (disk, ring))
  histTitle = gemGroupPrettyName+": "+correctionName
  
  h_dx.SetTitle(histTitle)
  fit = FitAndDraw(h_dx, littleLabel)
  legend.Draw()
  pngName = "GEM_dx_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
  pdfName = "GEM_dx_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  sRMS = "%.3f" % h_dx.GetRMS()
  gemGroupTable.FillGemGroup("dxRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
  if fit[0]:
    sSigma = "%.3f" % fit[1].GetParameter(2)
    gemGroupTable.FillGemGroup("dxGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
  
  h_dy.SetTitle(histTitle)
  fit = FitAndDraw(h_dy, littleLabel)
  legend.Draw()
  pngName = "GEM_dy_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
  pdfName = "GEM_dy_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  sRMS = "%.3f" % h_dy.GetRMS()
  gemGroupTable.FillGemGroup("dyRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
  if fit[0]:
    sSigma = "%.3f" % fit[1].GetParameter(2)
    gemGroupTable.FillGemGroup("dyGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
  
  h_dz.SetTitle(histTitle)
  fit = FitAndDraw(h_dz, littleLabel)
  legend.Draw()
  pngName = "GEM_dz_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
  pdfName = "GEM_dz_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  sRMS = "%.3f" % h_dz.GetRMS()
  gemGroupTable.FillGemGroup("dzRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
  if fit[0]:
    sSigma = "%.3f" % fit[1].GetParameter(2)
    gemGroupTable.FillGemGroup("dzGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
  
  h_dphix.SetTitle(histTitle)
  fit = FitAndDraw(h_dphix, littleLabel)
  legend.Draw()
  pngName = "GEM_dphix_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
  pdfName = "GEM_dphix_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  sRMS = "%.3f" % h_dphix.GetRMS()
  gemGroupTable.FillGemGroup("dphixRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
  if fit[0]:
    sSigma = "%.3f" % fit[1].GetParameter(2)
    gemGroupTable.FillGemGroup("dphixGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
  
  h_dphiy.SetTitle(histTitle)
  fit = FitAndDraw(h_dphiy, littleLabel)
  legend.Draw()
  pngName = "GEM_dphiy_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
  pdfName = "GEM_dphiy_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  sRMS = "%.3f" % h_dphiy.GetRMS()
  gemGroupTable.FillGemGroup("dphiyRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
  if fit[0]:
    sSigma = "%.3f" % fit[1].GetParameter(2)
    gemGroupTable.FillGemGroup("dphiyGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
  
  h_dphiz.SetTitle(histTitle)
  fit = FitAndDraw(h_dphiz, littleLabel)
  legend.Draw()
  pngName = "GEM_dphiz_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
  pdfName = "GEM_dphiz_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
  c1.SaveAs(pngPath+pngName)
  c1.SaveAs(pdfPath+pdfName)
  sRMS = "%.3f" % h_dphiz.GetRMS()
  gemGroupTable.FillGemGroup("dphizRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
  if fit[0]:
    sSigma = "%.3f" % fit[1].GetParameter(2)
    gemGroupTable.FillGemGroup("dphizGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)

#** Fit uncert: save plots and fill tables over homogeneous chambers *******

  if isReport:      
    histTitle = gemGroupPrettyName+": alignment fit uncertainties"
    
    h_ex.SetTitle(histTitle)
    fit = FitAndDraw(h_ex, alignmentName)
    legend.Draw()
    pngName = "GEM_ex_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_ex_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sMean = "%.3f" % h_ex.GetMean()
    gemGroupTable.FillGemGroup("exMean", endcap, disk, ring, sMean, "./PNG/"+pngName)
    if fit[0]:
      sGaussMean = "%.3f" % fit[1].GetParameter(1)
      gemGroupTable.FillGemGroup("exGaussMean", endcap, disk, ring, sGaussMean, "./PNG/"+pngName)
    
    h_ey.SetTitle(histTitle)
    fit = FitAndDraw(h_ey, alignmentName)
    legend.Draw()
    pngName = "GEM_ey_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_ey_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sMean = "%.3f" % h_ey.GetMean()
    gemGroupTable.FillGemGroup("eyMean", endcap, disk, ring, sMean, "./PNG/"+pngName)
    if fit[0]:
      sGaussMean = "%.3f" % fit[1].GetParameter(1)
      gemGroupTable.FillGemGroup("eyGaussMean", endcap, disk, ring, sGaussMean, "./PNG/"+pngName)
    
    h_ez.SetTitle(histTitle)
    fit = FitAndDraw(h_ez, alignmentName)
    legend.Draw()
    pngName = "GEM_ez_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_ez_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sMean = "%.3f" % h_ez.GetMean()
    gemGroupTable.FillGemGroup("ezMean", endcap, disk, ring, sMean, "./PNG/"+pngName)
    if fit[0]:
      sGaussMean = "%.3f" % fit[1].GetParameter(1)
      gemGroupTable.FillGemGroup("ezGaussMean", endcap, disk, ring, sGaussMean, "./PNG/"+pngName)
    
    h_ephix.SetTitle(histTitle)
    fit = FitAndDraw(h_ephix, alignmentName)
    legend.Draw()
    pngName = "GEM_ephix_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_ephix_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sMean = "%.3f" % h_ephix.GetMean()
    gemGroupTable.FillGemGroup("ephixMean", endcap, disk, ring, sMean, "./PNG/"+pngName)
    if fit[0]:
      sGaussMean = "%.3f" % fit[1].GetParameter(1)
      gemGroupTable.FillGemGroup("ephixGaussMean", endcap, disk, ring, sGaussMean, "./PNG/"+pngName)
    
    h_ephiy.SetTitle(histTitle)
    fit = FitAndDraw(h_ephiy, alignmentName)
    legend.Draw()
    pngName = "GEM_ephiy_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_ephiy_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sMean = "%.3f" % h_ephiy.GetMean()
    gemGroupTable.FillGemGroup("ephiyMean", endcap, disk, ring, sMean, "./PNG/"+pngName)
    if fit[0]:
      sGaussMean = "%.3f" % fit[1].GetParameter(1)
      gemGroupTable.FillGemGroup("ephiyGaussMean", endcap, disk, ring, sGaussMean, "./PNG/"+pngName)
    
    h_ephiz.SetTitle(histTitle)
    fit = FitAndDraw(h_ephiz, alignmentName)
    legend.Draw()
    pngName = "GEM_ephiz_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_ephiz_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sMean = "%.3f" % h_ephiz.GetMean()
    gemGroupTable.FillGemGroup("ephizMean", endcap, disk, ring, sMean, "./PNG/"+pngName)
    if fit[0]:
      sGaussMean = "%.3f" % fit[1].GetParameter(1)
      gemGroupTable.FillGemGroup("ephizGaussMean", endcap, disk, ring, sGaussMean, "./PNG/"+pngName)
      
#**** Pulls: save plots and fill tables over homogeneous chambers **********
    
    histTitle = gemGroupPrettyName+": pulls"
    
    h_px.SetTitle(histTitle)
    fit = FitAndDraw(h_px, littleLabel)
    legend.Draw()
    pngName = "GEM_px_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_px_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sRMS = "%.3f" % h_px.GetRMS()
    gemGroupTable.FillGemGroup("pxRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
    if fit[0]:
      sSigma = "%.3f" % fit[1].GetParameter(2)
      gemGroupTable.FillGemGroup("pxGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
    
    h_py.SetTitle(histTitle)
    fit = FitAndDraw(h_py, littleLabel)
    legend.Draw()
    pngName = "GEM_py_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_py_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sRMS = "%.3f" % h_py.GetRMS()
    gemGroupTable.FillGemGroup("pyRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
    if fit[0]:
      sSigma = "%.3f" % fit[1].GetParameter(2)
      gemGroupTable.FillGemGroup("pyGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
    
    h_pz.SetTitle(histTitle)
    fit = FitAndDraw(h_pz, littleLabel)
    legend.Draw()
    pngName = "GEM_pz_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_pz_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sRMS = "%.3f" % h_pz.GetRMS()
    gemGroupTable.FillGemGroup("pzRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
    if fit[0]:
      sSigma = "%.3f" % fit[1].GetParameter(2)
      gemGroupTable.FillGemGroup("pzGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
    
    h_pphix.SetTitle(histTitle)
    fit = FitAndDraw(h_pphix, littleLabel)
    legend.Draw()
    pngName = "GEM_pphix_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_pphix_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sRMS = "%.3f" % h_pphix.GetRMS()
    gemGroupTable.FillGemGroup("pphixRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
    if fit[0]:
      sSigma = "%.3f" % fit[1].GetParameter(2)
      gemGroupTable.FillGemGroup("pphixGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
    
    h_pphiy.SetTitle(histTitle)
    fit = FitAndDraw(h_pphiy, littleLabel)
    legend.Draw()
    pngName = "GEM_pphiy_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_pphiy_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sRMS = "%.3f" % h_pphiy.GetRMS()
    gemGroupTable.FillGemGroup("pphiyRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
    if fit[0]:
      sSigma = "%.3f" % fit[1].GetParameter(2)
      gemGroupTable.FillGemGroup("pphiyGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)
    
    h_pphiz.SetTitle(histTitle)
    fit = FitAndDraw(h_pphiz, littleLabel)
    legend.Draw()
    pngName = "GEM_pphiz_"+sEndcapPorM+"_%s_%s.png" % (disk, ring)
    pdfName = "GEM_pphiz_"+sEndcapPorM+"_%s_%s.pdf" % (disk, ring)
    c1.SaveAs(pngPath+pngName)
    c1.SaveAs(pdfPath+pdfName)
    sRMS = "%.3f" % h_pphiz.GetRMS()
    gemGroupTable.FillGemGroup("pphizRMS", endcap, disk, ring, sRMS, "./PNG/"+pngName)
    if fit[0]:
      sSigma = "%.3f" % fit[1].GetParameter(2)
      gemGroupTable.FillGemGroup("pphizGaussSig", endcap, disk, ring, sSigma, "./PNG/"+pngName)

#*******************************************************************************
#                        Auxiliarly output HTML files                           
#                           1. htmlName_d - file for corrections or biases      
#                           2. htmlName_e - file for fit uncertainties          
#                           3. htmlName_p - file for pulls                      
#*******************************************************************************

#************************* Corrections: print all DOF **************************

htmlFile_d = htmlPath + htmlName_d
texFile_d  = texPath  + texName_d

PrintHtmlHeader(htmlFile_d)
PrintTexHeader(texFile_d)

PrintHtmlCode(htmlFile_d,"<font size=\"+2\">Alignment %s for %s</font>" % (correctionName,alignmentName) )
PrintHtmlCode(htmlFile_d,"<p>")
PrintHtmlCode(htmlFile_d,"<table border=\"1\" cellpadding=\"5\">")
caption = "<font size=+1>%s</font> <br><font size=-1><pre>%s</pre></font>" % (correctionName, littleLabel)
PrintHtmlCode(htmlFile_d,"<caption>%s</caption>" % caption)
PrintHtmlCode(htmlFile_d,"<tr align=center>")
for dof in "x","y","z","phix","phiy","phiz": 
  pngName = "GEM_d%s.png" % dof
  PrintHtmlCode(htmlFile_d,"<td><a href=\"./PNG/%s\"><img src=\"./PNG/%s\" alt=\"text\" width=\"250\"></a></td>" % (pngName, pngName))
  if dof == "z": PrintHtmlCode(htmlFile_d,"</tr><tr align=center>")
PrintHtmlCode(htmlFile_d,"</tr>")
PrintHtmlCode(htmlFile_d,"</table>")

# Visualization

PrintHtmlCode(htmlFile_d,"<p>")
PrintHtmlCode(htmlFile_d,"<table border=\"1\" cellpadding=\"5\">")
caption = ("<font size=+1>Alignment %s visualization</font> <br><font size=-1>" % correctionName ) +alignmentName+" - "+referenceName+"</font>"
PrintHtmlCode(htmlFile_d,"<caption>%s</caption>" % caption)
for endcap in 1,2:
  PrintHtmlCode(htmlFile_d,"<tr align=center>")
#  for disk in 1,2,3,4:
  disk = 1
  if endcap == 1: diskPrettyName = "__GEp%s" % disk
  else:           diskPrettyName = "__GEm%s" % disk
  imageName = alignmentName+"-"+referenceName+diskPrettyName
  pngName = imageName+".png"
  PrintHtmlCode(htmlFile_d,"<td><a href=\"./PNG/%s\"><img src=\"./PNG/%s\" alt=\"text\" width=\"300\"></a></td>" % (pngName, pngName))
PrintHtmlCode(htmlFile_d,"</tr>")
PrintHtmlCode(htmlFile_d,"</table>")

PrintHtmlCode(htmlFile_d,"<p>")
caption = ("<font size=+1>Alignment %s averaged over homogeneous chambers</font> <br><font size=-1>" % correctionName )+alignmentName+" - "+referenceName+"</font>"
gemGroupTable.PrintHtml(htmlFile_d,["dxRMS","dyRMS","dzRMS","dphixRMS","dphiyRMS","dphizRMS"],caption,0)

PrintHtmlCode(htmlFile_d,"<p>")
caption = ("<font size=+1>Alignment %s averaged over homogeneous chambers</font> <br><font size=-1>" % correctionName )+alignmentName+" - "+referenceName+"</font>"
gemGroupTable.PrintHtml(htmlFile_d,["dxRMS","dxGaussSig","dyRMS","dyGaussSig","dzRMS","dzGaussSig","dphixRMS","dphixGaussSig","dphiyRMS","dphiyGaussSig","dphizRMS","dphizGaussSig"],caption,0)

#************************* Corrections: print separate DOF *********************

for dof in "x","y","z","phix","phiy","phiz":
  
  PrintHtmlCode(htmlFile_d,"<p>")
  
  if dof == "x":    htmlDof, texDof, unitDof = "&delta;x", "\\delta x", "mm"
  if dof == "y":    htmlDof, texDof, unitDof = "&delta;y", "\\delta y", "mm"
  if dof == "z":    htmlDof, texDof, unitDof = "&delta;z", "\\delta z", "mm"
  if dof == "phix": htmlDof, texDof, unitDof = "&delta;&phi;<sub>x</sub>", "\\delta \\phi_{x}", "mrad"
  if dof == "phiy": htmlDof, texDof, unitDof = "&delta;&phi;<sub>y</sub>", "\\delta \\phi_{y}", "mrad"
  if dof == "phiz": htmlDof, texDof, unitDof = "&delta;&phi;<sub>z</sub>", "\\delta \\phi_{z}", "mrad"
  
  htmlCaption = "<font size=+1>%s <i>%s</i> (%s) </font> <br><font size=-1><pre>%s</pre></font>" % (correctionName, htmlDof, unitDof, littleLabel)
  texCaption  = "%s $%s$~(%s) \\\\ {\\tiny \\verb;%s;}" % (correctionName, texDof, unitDof, littleLabel)
  if dof == "x": 
    gemTab_dx.PrintHtml(htmlFile_d, htmlCaption, 0)
    gemTab_dx.PrintTex(texFile_d, texCaption, "gemTab_dx", 0)
  if dof == "y":
    gemTab_dy.PrintHtml(htmlFile_d, htmlCaption, 0)
    gemTab_dy.PrintTex(texFile_d, texCaption, "gemTab_dy", 0)
  if dof == "z":
    gemTab_dz.PrintHtml(htmlFile_d, htmlCaption, 0)
    gemTab_dz.PrintTex(texFile_d, texCaption, "gemTab_dz", 0)
  if dof == "phix":
    gemTab_dphix.PrintHtml(htmlFile_d, htmlCaption, 0)
    gemTab_dphix.PrintTex(texFile_d, texCaption, "gemTab_dphix", 0)
  if dof == "phiy":
    gemTab_dphiy.PrintHtml(htmlFile_d, htmlCaption, 0)
    gemTab_dphiy.PrintTex(texFile_d, texCaption, "gemTab_dphiy", 0)
  if dof == "phiz":
    gemTab_dphiz.PrintHtml(htmlFile_d, htmlCaption, 0)
    gemTab_dphiz.PrintTex(texFile_d, texCaption, "gemTab_dphiz", 0)
  
  htmlCaption = ("<font size=+1>%s <i>%s</i> (%s) in homogeneous chambers</font> <br><font size=-1><pre>%s</pre></font>" % (correctionName, htmlDof, unitDof, littleLabel) )
  
  PrintHtmlCode(htmlFile_d,"<p>")
  PrintHtmlCode(htmlFile_d,"<table border=\"1\" cellpadding=\"5\">")
  PrintHtmlCode(htmlFile_d,"<caption>%s</caption>" % htmlCaption)
  PrintHtmlCode(htmlFile_d,"<tr align=center><th></th><th></th><th><i>Disk 1</i></th>")
  for endcap in 1,2:
    if endcap == 1: sEndcapPorM = "p"
    else:           sEndcapPorM = "m"
    ring = 1
#    for ring in 1,2,3:
        
    PrintHtmlCode( htmlFile_d, "<tr align=center>" )
    if ring == 1:
#if endcap == 1: PrintHtmlCode( htmlFile_d, "<th rowspan=\"3\"><i>GE+</i></th>" )
#     else:           PrintHtmlCode( htmlFile_d, "<th rowspan=\"3\"><i>GE-</i></th>" )
      if endcap == 1: PrintHtmlCode( htmlFile_d, "<th><i>GE+</i></th>" )
      else:           PrintHtmlCode( htmlFile_d, "<th><i>GE-</i></th>" )
    PrintHtmlCode( htmlFile_d, ("<th><i>Ring %s</i></th>" % ring) )
    disk = 1
#    for disk in 1,2,3,4:
    pngName = "GEM_d%s_%s_%s_%s.png" % (dof, sEndcapPorM, disk, ring)
    if disk != 1 and ring == 3: PrintHtmlCode( htmlFile_d, "<td>None</td>" )
    else: PrintHtmlCode( htmlFile_d, ("<td><a href=\"./PNG/%s\"><img src=\"./PNG/%s\" alt=\"text\" width=\"250\"></a></td>" % (pngName, pngName)) )
    PrintHtmlCode(htmlFile_d,"</tr>")
  PrintHtmlCode(htmlFile_d,"</table>")

PrintHtmlTrailer(htmlFile_d)
PrintTexTrailer(texFile_d)

#************************* Fit uncert: print all DOF ***************************

if isReport:
  htmlFile_e = htmlPath + htmlName_e
  texFile_e  = texPath  + texName_e
  
  PrintHtmlHeader(htmlFile_e)
  PrintTexHeader(texFile_e)
  
  PrintHtmlCode(htmlFile_e,"<font size=\"+2\">Alignment fit uncertainties for %s</font>" % alignmentName )
  PrintHtmlCode(htmlFile_e,"<p>")
  PrintHtmlCode(htmlFile_e,"<table border=\"1\" cellpadding=\"5\">")
  caption = "<font size=+1>Alignment fit uncertainties</font> <br><font size=-1>"+alignmentName+"</font>"
  PrintHtmlCode(htmlFile_e,"<caption>%s</caption>" % caption)
  PrintHtmlCode(htmlFile_e,"<tr align=center>")
  for dof in "x","y","z","phix","phiy","phiz": 
    pngName = "GEM_e"+dof+".png"
    PrintHtmlCode(htmlFile_e,"<td><a href=\"./PNG/%s\"><img src=\"./PNG/%s\" alt=\"text\" width=\"250\"></a></td>" % (pngName, pngName))
    if dof == "z": PrintHtmlCode(htmlFile_e,"</tr><tr align=center>")
  PrintHtmlCode(htmlFile_e,"</tr>")
  PrintHtmlCode(htmlFile_e,"</table>")

  PrintHtmlCode(htmlFile_e,"<p>")
  caption = "<font size=+1>Alignment fit uncertainties averaged over homogeneous chambers</font> <br><font size=-1>"+alignmentName+"</font>"
  gemGroupTable.PrintHtml(htmlFile_e,["exMean","eyMean","ezMean","ephixMean","ephiyMean","ephizMean"],caption,0)

  PrintHtmlCode(htmlFile_e,"<p>")
  caption = "<font size=+1>Alignment fit uncertainties averaged over homogeneous chambers</font> <br><font size=-1>"+alignmentName+"</font>"
  gemGroupTable.PrintHtml(htmlFile_e,["exMean","exGaussMean","eyMean","eyGaussMean","ezMean","ezGaussMean","ephixMean","ephixGaussMean","ephiyMean","ephiyGaussMean","ephizMean","ephizGaussMean"],caption,0)

#************************ Fit uncert: print separate DOF *********************

  for dof in "x","y","z","phix","phiy","phiz":
    
    PrintHtmlCode(htmlFile_e,"<p>")
    
    if dof == "x":    htmlDof, texDof, unitDof = "&sigma;<sub>fit</sub>x", "\\sigma_{fit} x", "mm"
    if dof == "y":    htmlDof, texDof, unitDof = "&sigma;<sub>fit</sub>y", "\\sigma_{fit} y", "mm"
    if dof == "z":    htmlDof, texDof, unitDof = "&sigma;<sub>fit</sub>z", "\\sigma_{fit} z", "mm"
    if dof == "phix": htmlDof, texDof, unitDof = "&sigma;<sub>fit</sub>&phi;<sub>x</sub>", "\\sigma_{fit} \\phi_{x}", "mrad"
    if dof == "phiy": htmlDof, texDof, unitDof = "&sigma;<sub>fit</sub>&phi;<sub>y</sub>", "\\sigma_{fit} \\phi_{y}", "mrad"
    if dof == "phiz": htmlDof, texDof, unitDof = "&sigma;<sub>fit</sub>&phi;<sub>z</sub>", "\\sigma_{fit} \\phi_{z}", "mrad"
    
    htmlCaption = ("<font size=+1><Alignment fit uncertainties <i>%s</i> (%s)</font> <br><font size=-1><pre>%s</pre></font>" % (htmlDof, unitDof, alignmentName))
    texCaption = "Alignment fit uncertainties $%s$~(%s) \\\\ {\\tiny \\verb;%s;}" % (texDof, unitDof, alignmentName)
    
    if dof == "x":
      gemTab_ex.PrintHtml(htmlFile_e, htmlCaption, 0)
      gemTab_ex.PrintTex(texFile_e, texCaption, "gemTab_ex", 0)
    if dof == "y":
      gemTab_ey.PrintHtml(htmlFile_e, htmlCaption, 0)
      gemTab_ey.PrintTex(texFile_e, texCaption, "gemTab_ey", 0)
    if dof == "z":
      gemTab_ez.PrintHtml(htmlFile_e, htmlCaption, 0)
      gemTab_ez.PrintTex(texFile_e, texCaption, "gemTab_ez", 0)
    if dof == "phix":
      gemTab_ephix.PrintHtml(htmlFile_e, htmlCaption, 0)
      gemTab_ephix.PrintTex(texFile_e, texCaption, "gemTab_ephix", 0)
    if dof == "phiy":
      gemTab_ephiy.PrintHtml(htmlFile_e, htmlCaption, 0)
      gemTab_ephiy.PrintTex(texFile_e, texCaption, "gemTab_ephiy", 0)
    if dof == "phiz":
      gemTab_ephiz.PrintHtml(htmlFile_e, htmlCaption, 0)
      gemTab_ephiz.PrintTex(texFile_e, texCaption, "gemTab_ephiz", 0)
    
    htmlCaption = ("<font size=+1><Alignment fit uncertainties <i>%s</i> (%s) in homogeneous chambers</font> <br><font size=-1><pre>%s</pre></font>" % (htmlDof, unitDof, alignmentName))
    
    PrintHtmlCode(htmlFile_e,"<p>")
    PrintHtmlCode(htmlFile_e,"<table border=\"1\" cellpadding=\"5\">")
    PrintHtmlCode(htmlFile_e,"<caption>%s</caption>" % htmlCaption)
    PrintHtmlCode(htmlFile_e,"<tr align=center><th></th><th></th><th><i>Disk 1</i></th>")
    for endcap in 1,2:
      if endcap == 1: sEndcapPorM = "p"
      else:           sEndcapPorM = "m"
      ring = 1
#for ring in 1,2,3:
      PrintHtmlCode( htmlFile_e, "<tr align=center>" )
      if ring == 1:
#if endcap == 1: PrintHtmlCode( htmlFile_e, "<th rowspan=\"3\"><i>GE+</i></th>" )
#       else:           PrintHtmlCode( htmlFile_e, "<th rowspan=\"3\"><i>GE-</i></th>" )
        if endcap == 1: PrintHtmlCode( htmlFile_e, "<th><i>GE+</i></th>" )
        else:           PrintHtmlCode( htmlFile_e, "<th><i>GE-</i></th>" )
      PrintHtmlCode( htmlFile_e, ("<th><i>Ring %s</i></th>" % ring) )
      disk = 1
#for disk in 1,2,3,4:
      pngName = "GEM_e%s_%s_%s_%s.png" % (dof, sEndcapPorM, disk, ring)
      if disk != 1 and ring == 3: PrintHtmlCode( htmlFile_e, "<td>None</td>" )
      else: PrintHtmlCode( htmlFile_e, ("<td><a href=\"./PNG/%s\"><img src=\"./PNG/%s\" alt=\"text\" width=\"250\"></a></td>" % (pngName, pngName)) )
      PrintHtmlCode(htmlFile_e,"</tr>")
    PrintHtmlCode(htmlFile_e,"</table>")

#***************************** Pulls: print all DOF ****************************
  
  htmlFile_p = htmlPath + htmlName_p
  texFile_p  = texPath  + texName_p
  
  PrintHtmlHeader(htmlFile_p)
  PrintTexHeader(texFile_p)
   
  PrintHtmlCode(htmlFile_p,"<font size=\"+2\">Pulls for %s</font>" % alignmentName )
  PrintHtmlCode(htmlFile_p,"<p>")
  PrintHtmlCode(htmlFile_p,"<table border=\"1\" cellpadding=\"5\">")
  caption = "<font size=+1>Pulls</font> <br><font size=-1>"+alignmentName+" - "+referenceName+"</font>"
  PrintHtmlCode(htmlFile_p,"<caption>%s</caption>" % caption)
  PrintHtmlCode(htmlFile_p,"<tr align=center>")
  for dof in "x","y","z","phix","phiy","phiz": 
   pngName = "GEM_p"+dof+".png"
   PrintHtmlCode(htmlFile_p,"<td><a href=\"./PNG/%s\"><img src=\"./PNG/%s\" alt=\"text\" width=\"250\"></a></td>" % (pngName, pngName))
   if dof == "z": PrintHtmlCode(htmlFile_p,"</tr><tr align=center>")
  
  PrintHtmlCode(htmlFile_p,"</tr>")
  PrintHtmlCode(htmlFile_p,"</table>")

  PrintHtmlCode(htmlFile_p,"<p>")
  caption = "<font size=+1>Pulls averaged over homogeneous chambers</font> <br><font size=-1>"+alignmentName+" - "+referenceName+"</font>"
  gemGroupTable.PrintHtml(htmlFile_p,["pxRMS","pyRMS","pzRMS","pphixRMS","pphiyRMS","pphizRMS"],caption,0)

  PrintHtmlCode(htmlFile_p,"<p>")
  caption = "<font size=+1>Pulls averaged over homogeneous chambers</font> <br><font size=-1>"+alignmentName+" - "+referenceName+"</font>"
  gemGroupTable.PrintHtml(htmlFile_p,["pxRMS","pxGaussSig","pyRMS","pyGaussSig","pzRMS","pzGaussSig","pphixRMS","pphixGaussSig","pphiyRMS","pphiyGaussSig","pphizRMS","pphizGaussSig"],caption,0)

#************************ Pulls: print separate DOF *********************

  for dof in "x","y","z","phix","phiy","phiz":
    
    PrintHtmlCode(htmlFile_p,"<p>")
    
    if dof == "x":    htmlDof, texDof = "x", "x"
    if dof == "y":    htmlDof, texDof = "y", "y"
    if dof == "z":    htmlDof, texDof = "z", "z"
    if dof == "phix": htmlDof, texDof = "&phi;<sub>x</sub>", "\\phi_{x}"
    if dof == "phiy": htmlDof, texDof = "&phi;<sub>y</sub>", "\\phi_{y}"
    if dof == "phiz": htmlDof, texDof = "&phi;<sub>z</sub>", "\\phi_{z}"
      
    htmlCaption = ("<font size=+1>Pulls for <i>%s</i></font> <br><font size=-1><pre>%s</pre></font>" % (htmlDof, littleLabel) )
    texCaption = ("Pulls for $%s$ \\\\ {\\tiny \\verb;%s;}" % (htmlDof, littleLabel) )
    
    if dof == "x":
      gemTab_px.PrintHtml(htmlFile_p, htmlCaption, 0)
      gemTab_px.PrintTex(texFile_p, texCaption, "gemTab_px", 0)
    if dof == "y":
      gemTab_py.PrintHtml(htmlFile_p, htmlCaption, 0)
      gemTab_py.PrintTex(texFile_p, texCaption, "gemTab_py", 0)
    if dof == "z":
      gemTab_pz.PrintHtml(htmlFile_p, htmlCaption, 0)
      gemTab_py.PrintTex(texFile_p, texCaption, "gemTab_py", 0)
    if dof == "phix":
      gemTab_pphix.PrintHtml(htmlFile_p, htmlCaption, 0)
      gemTab_pphix.PrintTex(texFile_p, texCaption, "gemTab_pphix", 0)
    if dof == "phiy":
      gemTab_pphiy.PrintHtml(htmlFile_p, htmlCaption, 0)
      gemTab_pphiy.PrintTex(texFile_p, texCaption, "gemTab_pphiy", 0)
    if dof == "phiz":
      gemTab_pphiz.PrintHtml(htmlFile_p, htmlCaption, 0)
      gemTab_pphiz.PrintTex(texFile_p, texCaption, "gemTab_pphiz", 0)
    
    caption = ("Pulls for <i>%s</i> in homogeneous chambers</font> <br><font size=-1><pre>%s</pre></font>" % (htmlDof, littleLabel))
    
    PrintHtmlCode(htmlFile_p,"<p>")
    PrintHtmlCode(htmlFile_p,"<table border=\"1\" cellpadding=\"5\">")
    PrintHtmlCode(htmlFile_p,"<caption>%s</caption>" % caption)
    PrintHtmlCode(htmlFile_p,"<tr align=center><th></th><th></th><th><i>Disk 1</i></th></tr>")
    for endcap in 1,2:
      PrintHtmlCode( htmlFile_p, "<tr align=center>" )
      if endcap == 1:
        sEndcapPorM = "p"
#PrintHtmlCode( htmlFile_p, "<th rowspan=\"3\"><i>GE+</i></th>" )
        PrintHtmlCode( htmlFile_p, "<th><i>GE+</i></th>" )
        
      else:
        sEndcapPorM = "m"
#PrintHtmlCode( htmlFile_p, "<th rowspan=\"3\"><i>GE-</i></th>" )
        PrintHtmlCode( htmlFile_p, "<th><i>GE-</i></th>" )
      ring = 1
      PrintHtmlCode( htmlFile_p, ("<th><i>Ring %s</i></th>" % ring) )
      disk = 1
      pngName = "GEM_p%s_%s_%s_%s.png" % (dof, sEndcapPorM, disk, ring)
      PrintHtmlCode( htmlFile_p, ("<td><a href=\"./PNG/%s\"><img src=\"./PNG/%s\" alt=\"text\" width=\"250\"></a></td>" % (pngName, pngName)) )
      PrintHtmlCode(htmlFile_p,"</tr>")
    PrintHtmlCode(htmlFile_p,"</table>")

  PrintHtmlTrailer(htmlFile_e)
  PrintHtmlTrailer(htmlFile_p)
