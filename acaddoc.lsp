(defun crest_insert (xy rotation)
  (command ".insert" "schoolcrest.dwg" xy "1" "1" rotation)
)

  
(defun C:crest ()
  (setq readVal (getint "Enter Number of Trophies, Default (10)"))
  (setq counter 0)
  (if (= readVal nil)
    (setq readVal 10)
    )
  
  (cond ((= (findfile "logopoints.txt") nil) ; if it cant find the file
	(ALERT "Fatal Error - Cannot find logopoints.txt")
	 ); end of first condition
	((= (findfile "schoolcrest.dwg") nil) ; if school crest is found
	 (ALERT "Fatal Error - Cannot find schoolcrest.dwg")
	 ); end of second condition
	(T  ;else do the actual insertions
	 (setq file (open (findfile "logopoints.txt") "r")); open file as file
         (while (and (setq txtLine (read-line file)) ; if counter is not reached and read_line succeded
		     (< counter readVal)
		     )
	     (setq counter (1+ counter))
             (crest_insert (substr txtLine 5) (substr txtline 1 3)) ;get 5- (co-ordinates) and 1-3 (rotation angle)
         )
	 )
	)
  (command "_regenall")
  (command "_regenall")
  (command "_regenall")
  (command "_regenall")
  (command "_regenall")
  (command "_regenall")
  (command "_regenall")
  (command "_regenall")
  (command "_regenall")
  (command "_regenall")
  (command "_regenall")
  )