Imports System.IO
Imports System.Reflection
Public Class AwardGenerator
    Public TROPHY_LIMITER As List(Of String)
    Public PLAQUE_LIMITER As List(Of String)
    Public EXE_PATH As String
    Public FileType As String
    Public FilePath As String
    Public Shared OpenNewName As String = "temp.txt"
    Public Shared ConfigFolder As String = ".settings_awards"
    Public ReadOnly TempTxtExport As String = "override.txt"
    Public Shared PossibleItems As String() = New String(1) {"SCHOOL_TROPHY", "SCHOOL_PLAQUE"}
    Public Shared DefaultItem As String = "SCHOOL_TROPHY"
    Public OverRideLocation As String
    Public JustSaved As Boolean
    Friend Enum SaveTypes
        TXT
        CSV
    End Enum
    'Load Helpers & document functions
    Public Sub Create_Hidden(foldername As String)
        If Not Directory.Exists(foldername) Then
            Directory.CreateDirectory(foldername)
        End If
        Dim Dinfo As DirectoryInfo = New DirectoryInfo(foldername)
        If ((Dinfo.Attributes & FileAttributes.Hidden)) <> FileAttributes.Hidden Then
            Dinfo.Attributes = Dinfo.Attributes Or FileAttributes.Hidden
        End If
    End Sub

    Private Sub ProgramLoad(sender As Object, e As EventArgs) Handles MyBase.Load
        DataTable.DataMember = "AwardTable"
        JustSaved = True
        PLAQUE_LIMITER = New List(Of String)
        TROPHY_LIMITER = New List(Of String)
        Create_Hidden(ConfigFolder)
        Extract_Exe()
        FileType = SaveTypes.TXT
        FilePath = ""
        UpdateButtons()
    End Sub


    Public Sub Write_Config(Path As String)

    End Sub

    Public Sub Read_Config(Path As String)

    End Sub

    Public Sub Extract_Exe(Optional exepath As String = Nothing, Optional exename As String = "parser.exe")
        If exepath Is Nothing Then
            exepath = ConfigFolder
        End If
        exepath = Path.Combine(exepath, exename)
        Dim currassembly As Assembly = Assembly.GetExecutingAssembly()
        Dim exestream As Stream = currassembly.GetManifestResourceStream("VisualProject.parser.exe")
        File.WriteAllBytes(exepath, ReadFully(exestream))
        EXE_PATH = exepath
    End Sub

    Private Sub OnKeyDownForm(ByVal sender As Object, ByVal e As KeyEventArgs) Handles MyBase.KeyDown
        If (e.Control AndAlso e.Shift AndAlso (e.KeyCode = Keys.S)) Then
            ' When control and S press ave as
            SaveAsPromptWrapper()
        ElseIf (e.Control AndAlso (e.KeyCode = Keys.S)) Then
            ' control-s = SAVE
            SaveFilesAbsolute()
        ElseIf (e.Control AndAlso (e.KeyCode = Keys.E)) Then
            'control-e = Export
            ExportAsDXFWrapper()
        End If
    End Sub







    'Add, Remove, Change Wrappers
    Public Sub AddRowTable(Award As String, Name As String, Year As String)
        DataTable.Rows.Add(Award, Name, Year)
        UpdateButtons()
    End Sub

    Public Sub ChangeRowTable(RowIndex As Integer, AwardType As String, Name As String, Year As String)
        DataTable.Rows(RowIndex).Cells(0).Value = AwardType
        DataTable.Rows(RowIndex).Cells(1).Value = Name
        DataTable.Rows(RowIndex).Cells(2).Value = Year
    End Sub

    ' Adds A Row
    Public Sub AddRowWrapper()
        Dim SecondForm As New AddForm
        If SecondForm.ShowDialog() = DialogResult.OK Then
            Dim templist As List(Of String) = SecondForm.GetTextRow
            DataTable.Rows.Add(templist(0), templist(1), templist(2))
        End If
        UpdateButtons()
    End Sub

    Private Sub AddRow_Click(sender As Object, e As EventArgs) Handles AddRow.Click
        AddRowWrapper()
    End Sub

    'Removes A Row
    Public Sub RemoveRowWrapper()
        Dim RowDictionary As New SortedDictionary(Of Integer, Integer)
        For Each Cell As DataGridViewCell In DataTable.SelectedCells
            If Not RowDictionary.ContainsKey(Cell.RowIndex) Then
                RowDictionary.Add(Cell.RowIndex, 1)
            End If
        Next
        For Each Item As KeyValuePair(Of Integer, Integer) In RowDictionary.Reverse
            Try
                DataTable.Rows.RemoveAt(Item.Key)
            Catch ex As InvalidOperationException
            End Try
        Next
        UpdateButtons()
    End Sub

    Private Sub RemoveRow_Click(sender As Object, e As EventArgs) Handles RemoveRow.Click
        RemoveRowWrapper()
    End Sub

    'Edits A Row
    Public Sub EditRowWrapper()
        If DataTable.SelectedCells.Count > 0 Then
            Dim RowDictionary As New SortedDictionary(Of Integer, Integer)
            For Each Cell As DataGridViewCell In DataTable.SelectedCells
                If Not RowDictionary.ContainsKey(Cell.RowIndex) Then
                    RowDictionary.Add(Cell.RowIndex, 1)
                End If
            Next
            Dim SecondForm As New ChangeForm
            Dim RowNumber As Integer
            For Each temp As KeyValuePair(Of Integer, Integer) In RowDictionary
                RowNumber = temp.Key
                Exit For
            Next
            SecondForm.FillForm(RowNumber, DataTable.Rows(RowNumber).Cells(0).Value, DataTable.Rows(RowNumber).Cells(1).Value, DataTable.Rows(RowNumber).Cells(2).Value)
            If SecondForm.ShowDialog() = DialogResult.OK Then
                Dim templist As ArrayList = SecondForm.GetEditItem
                ChangeRowTable(templist(0), templist(1), templist(2), templist(3))
            End If

        End If
        UpdateButtons()
    End Sub






    'Helper Functions
    Public Function ReadFully(input As Stream) As Byte()
        Dim buffer(input.Length) As Byte
        Using br As New BinaryReader(input)
            buffer = br.ReadBytes(input.Length)
        End Using
        Return buffer.ToArray
    End Function

    Public Function FormatStringArray(StringArray As String()) As String()
        Dim templist As List(Of String) = StringArray.ToList
        templist.RemoveAll(AddressOf String.IsNullOrEmpty)
        Return templist.ToArray
    End Function

    Public Function RemoveFirstAndLast(StringArray As String()) As String()
        Dim ret As New List(Of String)
        For counter As Integer = 1 To StringArray.Length - 2
            ret.Add(StringArray(counter))
        Next counter
        Return ret.ToArray
    End Function

    Public Function FormatSaveType(item As String) As String
        Select Case item
            Case "0"
                Return "TXT"
            Case "1"
                Return "CSV"
            Case "2"
                Return "NONE"
            Case Else
                Return "???"
        End Select
    End Function

    Public Function GenerateStreamFromArray(StringArray As String()) As Stream
        Dim stream As New MemoryStream()
        Dim writer As New StreamWriter(stream)
        For Each Line As String In StringArray
            writer.WriteLine(Line)
        Next
        writer.Flush()
        stream.Position = 0
        Return stream
    End Function


    'Export And Import Wrappers
    'Export As CSV
    Public Sub ExportCSV(outPath As String)
        Try
            Using outStream As StreamWriter = New StreamWriter(outPath)
                If outStream IsNot Nothing Then
                    For Each row As DataGridViewRow In DataTable.Rows
                        If Not row.IsNewRow Then
                            Try
                                outStream.WriteLine(String.Format("""{0}"",""{1}"",""{2}""", row.Cells(0).Value.Replace("""", """"""),
                                                                                            row.Cells(1).Value.Replace("""", """"""),
                                                                                            row.Cells(2).Value.Replace("""", """""")))
                            Catch ex As Exception
                                MsgBox("Error on line" & row.Cells(0).ToString & ex.ToString)
                            End Try
                        End If
                    Next
                Else
                    MsgBox("the fileStream cannot be written to")
                End If
            End Using


        Catch ex As IOException
            MsgBox("The disk is full or file exists and is readonly")
        Catch ex As Exception
            MsgBox("an error occured! i dont know what happened >:L" & ex.ToString)
        End Try
    End Sub

    ' Read As CSV
    Private Sub ParseCsv(ResourcePath As String)
        Dim WrongLineNumber As New ArrayList
        'Dim WrongLineText As New ArrayList
        Dim WrongLineReason As New ArrayList
        Dim LineNumber As Integer = 0
        Dim TrophyNumber As Integer = 0
        Dim ErrorMessage As Text.StringBuilder = New Text.StringBuilder


        Dim Warning As Boolean = False
        Dim Fields() As String
        If File.Exists(ResourcePath) = True Then
            Try
                Using parser As FileIO.TextFieldParser = New FileIO.TextFieldParser(ResourcePath)
                    parser.TextFieldType = FileIO.FieldType.Delimited
                    parser.SetDelimiters(",")
                    parser.HasFieldsEnclosedInQuotes = True

                    Dim AskedDefault = False
                    While Not parser.EndOfData
                        ' first incremenet the counter vars
                        LineNumber += 1

                        Try
                            Fields = FormatStringArray(parser.ReadFields())
                        Catch ex As FileIO.MalformedLineException
                            WrongLineNumber.Add(LineNumber)
                            WrongLineReason.Add("Line cannot be parsed!")
                            Warning = True
                            Continue While
                        End Try


                        If Fields.Length < 2 Then
                            WrongLineNumber.Add(LineNumber)
                            WrongLineReason.Add("Line is too short! " & String.Join(",", Fields))

                        ElseIf Fields.Length = 2 Then

                            If Not AskedDefault Then
                                MsgBox("Assuming 2-length lines as " & DefaultItem & "'s")
                                AskedDefault = True
                            End If
                            DataTable.Rows.Add(DefaultItem, Fields(0), Fields(1))
                        Else
                            If PossibleItems.Contains(Fields(0)) Then
                                DataTable.Rows.Add(Fields(0), String.Join(" ", RemoveFirstAndLast(Fields)), Fields(Fields.Length - 1))
                                TrophyNumber += 1
                            Else
                                Dim templist As List(Of String) = Fields.ToList
                                templist.RemoveAt(templist.Count - 1)
                                DataTable.Rows.Add(DefaultItem, String.Join(" ", templist.ToArray), Fields(Fields.Length - 1))
                                TrophyNumber += 1

                            End If

                        End If

                    End While

                    If Warning Then
                        MsgBox(WrongLineNumber.Count)
                        For counter As Integer = 0 To WrongLineNumber.Count - 1
                            Dim _LineNum As Integer = WrongLineNumber(counter)
                            'Dim _Text As String = WrongLineText(counter)
                            Dim _Reason As String = WrongLineReason(counter)
                            ErrorMessage.Append(String.Format("Error on Line {0}: {1}", _LineNum, _Reason) & Environment.NewLine)
                        Next counter
                        MessageBox.Show(ErrorMessage.ToString, "Non-fatal errors on parsing document", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
                    End If
                    ' enable all the buttons
                    JustSaved = False

                End Using
            Catch ex As IOException
                MessageBox.Show("The file cannot be accessed. Ensure no other programs are using this file and retry",
                            "File IO Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Catch ex As Exception
                MessageBox.Show("An error occured :(" & ex.ToString)
            End Try
        Else
            MessageBox.Show("The File Can no longer be found?!")
        End If
    End Sub

    ' WRAPS ParseCsv, Error checking
    Public Sub ImportCSV(CsvPath As String)
        If CsvPath.StartsWith("~") Then
            CsvPath = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile) & CsvPath.Remove(0, 1)
        End If
        If Not My.Computer.FileSystem.FileExists(CsvPath) Then
            MessageBox.Show("Path not found! Please double check value in text box", "Invalid Path", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Exit Sub
        End If
        ' Passed all tests!
        ParseCsv(CsvPath)
        UpdateButtons()
    End Sub

    ' Export As Txt
    Public Sub ExportTxt(outPath As String)
        Using txtwriter As New StreamWriter(outPath)
            txtwriter.WriteLine("{CSV}")
            For Each row As DataGridViewRow In DataTable.Rows
                txtwriter.WriteLine(String.Format("""{0}"",""{1}"",""{2}""", row.Cells(0).Value.ToString.Replace("""", """"""),
                                                              row.Cells(1).Value.ToString.Replace("""", """"""),
                                                              row.Cells(2).Value.ToString.Replace("""", """""")))
            Next
            If TROPHY_LIMITER.Count <> 0 Then
                txtwriter.WriteLine("{TROPHY_LIMITER}")
                For z = 0 To NoSheets - 1
                    txtwriter.WriteLine(String.Join(" ", TROPHY_LIMITER.ConvertAll(Function(i As Integer) i.ToString())))
                Next

            End If
            If PLAQUE_LIMITER.Count <> 0 Then
                txtwriter.WriteLine("{PLAQUE_LIMITER}")
                txtwriter.WriteLine(String.Join(" ", PLAQUE_LIMITER.ConvertAll(Function(i As Integer) i.ToString())))
            End If
        End Using
    End Sub

    ' Read As TXT
    Private Sub ParseTxt(ResourcePath As String)
        Dim CurrentIdentity As String = String.Empty
        Dim stringArray As New List(Of String)
        For Each Line As String In File.ReadLines(ResourcePath)
            Dim processed = Line.ToLower
            If processed = "{csv}" Then
                CurrentIdentity = "CSV"
            ElseIf processed = "{trophy_limiter}" Then
                CurrentIdentity = "T_LIMIT"
            ElseIf processed = "{plauqe_limiter}" Then
                CurrentIdentity = "P_LIMIT"
            Else
                Select Case (CurrentIdentity)
                    Case "P_LIMIT"
                        PLAQUE_LIMITER = (Line.Split(" ").ToList)
                    Case "T_LIMIT"
                        TROPHY_LIMITER = (Line.Split(" ").ToList)
                    Case "CSV"
                        stringArray.Add(Line)
                End Select
            End If
        Next
        Dim AskDefault As Boolean = False
        Using parser As FileIO.TextFieldParser = New FileIO.TextFieldParser(GenerateStreamFromArray(stringArray.ToArray))
            parser.TextFieldType = FileIO.FieldType.Delimited
            parser.SetDelimiters(",")
            parser.HasFieldsEnclosedInQuotes = True
            While Not parser.EndOfData
                Try
                    Dim line = FormatStringArray(parser.ReadFields())
                    If line.Length < 3 Then
                        MsgBox("errpr" & String.Join(" ", line))

                    Else
                        DataTable.Rows.Add(line(0), String.Join(" ", RemoveFirstAndLast(line)), line(line.Length - 1))

                    End If

                Catch ex As Exception
                    MsgBox("error" & ex.ToString)
                End Try
            End While
        End Using
    End Sub

    ' Wraps ParseTxt, Error checking
    Public Sub ImportTxt(TxtPath As String)
        If TxtPath.StartsWith("~") Then
            TxtPath = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile) & TxtPath.Remove(0, 1)
        End If
        If Not My.Computer.FileSystem.FileExists(TxtPath) Then
            MessageBox.Show("Path not found! Please double check value in text box", "Invalid Path", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Exit Sub
        End If
        ' Passed all tests!

        ParseTxt(TxtPath)
        UpdateButtons()
    End Sub

    ' Save/Load/Export
    Public Sub SaveAsPromptWrapper(Optional SaveDialogObject As SaveFileDialog = Nothing)
        If Object.ReferenceEquals(SaveDialogObject, Nothing) Then
            SaveDialogObject = SaveAsPrompt
        End If
        If SaveDialogObject.ShowDialog = DialogResult.OK Then
            Select Case SaveDialogObject.FilterIndex
                ' selected txt
                Case 1
                    FileType = SaveTypes.TXT
                    ExportTxt(SaveDialogObject.FileName)
                Case 2
                    FileType = "CSV"
                    ExportCSV(SaveAsPrompt.FileName)
                Case Else
                    MsgBox("? BAD HAPPENED")
            End Select
            FilePath = SaveDialogObject.FileName
        End If
    End Sub

    Public Sub OpenAsPromptWrapper(Optional ChangeFilePath = True)
        If OpenAsPrompt.ShowDialog() = DialogResult.OK Then
            If OpenAsPrompt.FileName.ToLower.EndsWith(".csv") Then
                ImportCSV(OpenAsPrompt.FileName)
                If ChangeFilePath = True Then
                    FileType = SaveTypes.CSV
                End If
            Else
                ImportTxt(OpenAsPrompt.FileName)
                If ChangeFilePath = True Then
                    FileType = SaveTypes.TXT
                End If
            End If
            If ChangeFilePath = True Then
                FilePath = OpenAsPrompt.FileName
            End If
        End If
    End Sub

    Public Sub SaveFilesAbsolute()
        If FilePath = String.Empty Then
            FilePath = (New DirectoryInfo(Path.Combine(ConfigFolder, OpenNewName))).FullName
        End If
        If FileType = SaveTypes.TXT Then
            ExportTxt(FilePath)
        ElseIf FileType = SaveTypes.CSV Then
            ExportCSV(FilePath)
        End If
    End Sub

    Public Sub ExportAsDXFWrapper()
        Dim OptionsArray As New List(Of String)
        If ExportAsPrompt.ShowDialog = DialogResult.OK Then
            OptionsArray.Add("-f " & """" & ExportAsPrompt.FileName & """")
        Else
            Exit Sub
        End If
        SaveFilesAbsolute()

        If FileType = SaveTypes.TXT Then
            OptionsArray.Add("-t")
        ElseIf FileType = SaveTypes.CSV Then
            OptionsArray.Add("-c")
        End If

        MsgBox(EXE_PATH & " " & String.Join(" ", OptionsArray) & " " & """" & FilePath & """")
        Clipboard.SetText(EXE_PATH & " " & String.Join(" ", OptionsArray) & " " & """" & FilePath & """")
        Shell(EXE_PATH & " " & String.Join(" ", OptionsArray) & " " & """" & FilePath & """")
    End Sub

    ' Change
    Private Sub ChangeRowButton_Click(sender As Object, e As EventArgs) Handles ChangeRowButton.Click
        EditRowWrapper()
    End Sub





    Private NoSheets As Integer
    ' Delimiters
    Public Sub SetLimiterWrapper()
        If FileType <> SaveTypes.TXT Then
            MessageBox.Show("The item is in CSV format: It will be re-saved to a TXT file")
            SaveAsPromptWrapper(OnlyTXTSave)
        End If
            Dim ThirdForm As New ChooseLimiters(TROPHY_LIMITER, PLAQUE_LIMITER, GetTrophyNumber(), GetPlaqueNumber())
        If ThirdForm.ShowDialog() = DialogResult.OK Then
            Me.TROPHY_LIMITER = ThirdForm.TROPHY_LIMITER
            NoSheets = ThirdForm.TrophyNumberSheets
        End If
    End Sub
    Private Sub SetLimiters_Click(sender As Object, e As EventArgs) Handles SetLimiters.Click
        SetLimiterWrapper()
    End Sub

    Public Function GetTrophyNumber() As Integer
        Dim Ret = 0
        For Each TempRow As DataGridViewRow In DataTable.Rows
            If TempRow.Cells(0).Value = "SCHOOL_TROPHY" Then
                Ret += 1
            End If
        Next
        Return Ret
    End Function

    Public Function GetPlaqueNumber() As Integer
        Dim Ret = 0
        For Each TempRow As DataGridViewRow In DataTable.Rows
            If TempRow.Cells(0).Value = "SCHOOL_PLAQUE" Then
                Ret += 1
            End If
        Next
        Return Ret
    End Function


    ' Event Handlers
    ' Open in Toolstrip
    Private Sub OpenToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles OpenToolStripMenuItem.Click
        If DataTable.Rows.Count <> 0 Then
            If MessageBox.Show("There is content in current table that would be lost. Are you sure?", "Verify", MessageBoxButtons.OKCancel,
                           MessageBoxIcon.Exclamation, MessageBoxDefaultButton.Button2) = DialogResult.Cancel Then
                Exit Sub
            End If
        End If
        DataTable.Rows.Clear()
        OpenAsPromptWrapper()
    End Sub

    'Add To.. In Toolstrip
    Private Sub AddFileToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles AddFileToolStripMenuItem.Click
        Try
            OpenAsPromptWrapper(False)
        Catch ex As Exception
            MsgBox("I dont know what happened >:(" & ex.ToString)
        End Try
    End Sub

    'Save As in Toolstrip
    Private Sub SaveAsToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles SaveAsToolStripMenuItem.Click
        SaveAsPromptWrapper()
    End Sub

    'Save in toolstrip
    Private Sub SaveToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles SaveToolStripMenuItem.Click
        SaveFilesAbsolute()
    End Sub

    'Shows FileInfo
    Private Sub FileInfo_Click_(sender As Object, e As EventArgs) Handles FileInfo.Click
        Dim TempFilePath As String
        Dim TempOverride As String
        If FilePath = String.Empty Then
            TempFilePath = "None"
        Else
            TempFilePath = FilePath
        End If
        If OverRideLocation <> Nothing Then
            TempOverride = OverRideLocation
        Else
            TempOverride = "None"
        End If
        MessageBox.Show("File Path: " & TempFilePath & Environment.NewLine &
                    "File Type: " & FormatSaveType(FileType) & Environment.NewLine &
                    "Override: " & TempOverride & Environment.NewLine)
    End Sub


    Public Sub UpdateButtons()
        If DataTable.Rows.Count <= 0 Then
            SetLimiters.Enabled = False
            ChangeRowButton.Enabled = False
        Else
            SetLimiters.Enabled = True
            ChangeRowButton.Enabled = True
        End If
    End Sub

    Private Sub FileToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles FileToolStripMenuItem.Click

    End Sub

    Private Sub ExportToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles ExportToolStripMenuItem.Click
        ExportAsDXFWrapper()
    End Sub

    Private Sub MenuStrip1_ItemClicked(sender As Object, e As ToolStripItemClickedEventArgs) Handles MenuStrip1.ItemClicked

    End Sub

End Class