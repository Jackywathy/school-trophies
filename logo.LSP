(defun ins (xy)
(command "_insert" "C:\\Users\\Jack Jiang\\Downloads\\crestn.dxf" xy "0.012" "0.012" "270")  
)

  
(defun runfile ()
  if (setq f (open "C:\\Users\\Jack Jiang\\Desktop\\school-trophies\\logopoints.txt" "r"))
  (while (setq txtLine(read-line f))
    (print txtline)
    (ins txtLine)
  )
  )