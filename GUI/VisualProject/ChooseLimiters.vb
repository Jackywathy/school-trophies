Public Class ChooseLimiters
    Sub New(ByVal TROPHY_L As List(Of String), ByVal PLAQUE_L As List(Of String), ByVal TotalTrophies As Integer, ByVal TotalPlaque As Integer)
        ' This call is required by the designer.
        InitializeComponent()
        ' Add any initialization after the InitializeComponent() call.
        TROPHY_LIMITER = TROPHY_L
        PLAQUE_LIMITER = PLAQUE_L
        Me.TotalTrophies = TotalTrophies
        Me.TotalPlaque = TotalPlaque
        TrophyEnabled = True
        DoNotChange = False

        AddCheckBoxes()
        LoadFromList(TROPHY_L)
        UpdateUI()

    End Sub

    Public TrophyEnabled As Boolean
    Public TrophyNumberSheets As Integer
    Public PlaqueNumberSheets As Integer
    Public TotalTrophies As Integer
    Public TotalPlaque As Integer

    Public TROPHY_LIMITER As List(Of String)
    Public PLAQUE_LIMITER As List(Of String)

    Private CheckBoxList As List(Of CheckBox)
    Private Columns As List(Of List(Of CheckBox))

    Private Sub ChooseLimiters_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        NoTrophy.Text = Me.TotalTrophies.ToString
    End Sub

    Private Sub SetAllCheckBoxesAsDisabled()
        For Each I As CheckBox In CheckBoxList
            If Not I.Checked Then
                I.Enabled = False
            End If
        Next
    End Sub

    Public Function GetCurrentlySelected() As Integer
        Dim ret = 0
        For Each i As CheckBox In CheckBoxList
            If i.Checked Then
                ret += 1
            End If
        Next
        Return ret
    End Function
    Private DoNotChange As Boolean

    Public Sub ProcessCheckBox(IntArray As Integer(), ByVal sender As CheckBox)
        If DoNotChange Then
            DoNotChange = False
            Exit Sub
        End If
        If AllChecked(IntArray) Or TrophyEnabled = False Then
            For Each I As Integer In IntArray
                CheckBoxList(I).Checked = False
            Next
        Else
            Dim CurrentCounter = GetCurrentlySelected()

            For Each i As Integer In IntArray
                If CurrentCounter >= TotalTrophies Then
                    Exit Sub
                Else
                    If Not CheckBoxList(i).Checked Then
                        CurrentCounter += 1
                        CheckBoxList(i).Checked = True
                    End If
                End If
            Next
        End If
    End Sub

    Private Function AllChecked(IntArray As Integer()) As Boolean
        For Each i As Integer In IntArray
            If Not CheckBoxList(i).Checked Then
                Return False
            End If
        Next
        Return True
    End Function
    Private Sub LoadFromList(OfList As List(Of String))
        For Each che As CheckBox In CheckBoxList
            che.Checked = False
        Next
        For Each str As String In OfList
            CheckBoxList(Integer.Parse(str)).Checked = True
        Next
    End Sub



    Private CheckTrophyCol1 As List(Of CheckBox)
    Private CheckTrophyCol2 As List(Of CheckBox)
    Private CheckTrophyCol3 As List(Of CheckBox)

    Private CheckTrophyRow1 As List(Of CheckBox)
    Private CheckTrophyRow2 As List(Of CheckBox)
    Private CheckTrophyRow3 As List(Of CheckBox)
    Private CheckTrophyRow4 As List(Of CheckBox)

    Private CheckTrophyBack1 As List(Of CheckBox)
    Private CheckTrophyBack2 As List(Of CheckBox)
    Private CheckTrophyBack3 As List(Of CheckBox)
    Private CheckTrophyBack4 As List(Of CheckBox)

    Private MapCheckBox As Dictionary(Of CheckBox, List(Of CheckBox))
    Private Sub AddCheckBoxes()
        CheckBoxList = New List(Of CheckBox)
        CheckTrophyCol1 = New List(Of CheckBox)
        CheckTrophyCol2 = New List(Of CheckBox)
        CheckTrophyCol3 = New List(Of CheckBox)

        CheckTrophyRow1 = New List(Of CheckBox)
        CheckTrophyRow2 = New List(Of CheckBox)
        CheckTrophyRow3 = New List(Of CheckBox)
        CheckTrophyRow4 = New List(Of CheckBox)

        CheckTrophyBack1 = New List(Of CheckBox)
        CheckTrophyBack2 = New List(Of CheckBox)
        CheckTrophyBack3 = New List(Of CheckBox)
        CheckTrophyBack4 = New List(Of CheckBox)

        MapCheckBox = New Dictionary(Of CheckBox, List(Of CheckBox))

        CheckBoxList.AddRange(New CheckBox() {Trophy0, Trophy1, Trophy2, Trophy3, Trophy4, Trophy5, Trophy6, Trophy7, Trophy8, Trophy9})

        CheckTrophyCol1.AddRange(New CheckBox() {Trophy3, Trophy2, Trophy1, Trophy0})
        CheckTrophyCol2.AddRange(New CheckBox() {Trophy7, Trophy6, Trophy5, Trophy4})
        CheckTrophyCol3.AddRange(New CheckBox() {Trophy9, Trophy8})

        CheckTrophyRow4.AddRange(New CheckBox() {Trophy3, Trophy7})
        CheckTrophyRow3.AddRange(New CheckBox() {Trophy2, Trophy6})
        CheckTrophyRow2.AddRange(New CheckBox() {Trophy1, Trophy5})
        CheckTrophyRow1.AddRange(New CheckBox() {Trophy0, Trophy4})

        CheckTrophyBack4.AddRange(New CheckBox() {Trophy9, Trophy7, Trophy3})
        CheckTrophyBack3.AddRange(New CheckBox() {Trophy9, Trophy6, Trophy2})
        CheckTrophyBack2.AddRange(New CheckBox() {Trophy8, Trophy5, Trophy1})
        CheckTrophyBack1.AddRange(New CheckBox() {Trophy8, Trophy4, Trophy0})

        MapCheckBox.Add(TrophyRowLeft4, CheckTrophyRow4)
        MapCheckBox.Add(TrophyRowLeft3, CheckTrophyRow3)
        MapCheckBox.Add(TrophyRowLeft2, CheckTrophyRow2)
        MapCheckBox.Add(TrophyRowLeft1, CheckTrophyRow1)

        MapCheckBox.Add(TrophyRowRight4, CheckTrophyBack4)
        MapCheckBox.Add(TrophyRowRight3, CheckTrophyBack3)
        MapCheckBox.Add(TrophyRowRight2, CheckTrophyBack2)
        MapCheckBox.Add(TrophyRowRight1, CheckTrophyBack1)

        MapCheckBox.Add(TrophyCol1, CheckTrophyCol1)
        MapCheckBox.Add(TrophyCol2, CheckTrophyCol2)
        MapCheckBox.Add(TrophyCol3, CheckTrophyCol3)
    End Sub

    Private Sub TrophyCol3_Click(sender As Object, e As EventArgs) Handles TrophyCol3.CheckedChanged
        ProcessCheckBox(New Integer() {8, 9}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyCol2_Click(sender As Object, e As EventArgs) Handles TrophyCol2.CheckedChanged
        ProcessCheckBox(New Integer() {7, 6, 5, 4}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyCol1_Click(sender As Object, e As EventArgs) Handles TrophyCol1.CheckedChanged
        ProcessCheckBox(New Integer() {0, 1, 2, 3}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyRowLeft4_Click(sender As Object, e As EventArgs) Handles TrophyRowLeft4.CheckedChanged
        ProcessCheckBox(New Integer() {3, 7}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyRowLeft3_Click(sender As Object, e As EventArgs) Handles TrophyRowLeft3.CheckedChanged
        ProcessCheckBox(New Integer() {2, 6}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyRowLeft2_Click(sender As Object, e As EventArgs) Handles TrophyRowLeft2.CheckedChanged
        ProcessCheckBox(New Integer() {1, 5}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyRowLeft1_Click(sender As Object, e As EventArgs) Handles TrophyRowLeft1.CheckedChanged
        ProcessCheckBox(New Integer() {0, 4}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyRowRight1_Click(sender As Object, e As EventArgs) Handles TrophyRowRight1.CheckedChanged
        ProcessCheckBox(New Integer() {8, 4, 0}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyRowRight2_Click(sender As Object, e As EventArgs) Handles TrophyRowRight2.CheckedChanged
        ProcessCheckBox(New Integer() {8, 5, 1}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyRowRight3_Click(sender As Object, e As EventArgs) Handles TrophyRowRight3.CheckedChanged
        ProcessCheckBox(New Integer() {9, 6, 2}, DirectCast(sender, CheckBox))
    End Sub

    Private Sub TrophyRowRight4_Click(sender As Object, e As EventArgs) Handles TrophyRowRight4.CheckedChanged
        ProcessCheckBox(New Integer() {9, 7, 3}, DirectCast(sender, CheckBox))
    End Sub

    Public Function GetCurrentlySelectedOr10() As Integer
        Dim ret = 0
        For Each i As CheckBox In CheckBoxList
            If i.Checked Then
                ret += 1
            End If
        Next
        Return If(ret <> 0, ret, 10)
    End Function

    Private Sub UpdateUI()

        Dim currentAlloc = GetCurrentlySelectedOr10()

        NumberSheet.Text = currentAlloc
        TrophyNumberSheets = Math.Ceiling(TotalTrophies / currentAlloc)
        TrophiesPerSheet.Text = currentAlloc
        NumberSheet.Text = TrophyNumberSheets.ToString

    End Sub

    Private Sub CancelButton_Click(sender As Object, e As EventArgs) Handles CancelButtonTrophy.Click
        Me.DialogResult = DialogResult.Cancel
        Close()
    End Sub

    Private TrophyCount As Integer
    Private PlaqueCount As Integer

    Public Function EnumerateFromZeroToInt(upto As Integer, Optional skip As List(Of Integer) = Nothing) As List(Of String)
        If skip Is Nothing Then
            skip = New List(Of Integer)
        End If
        Dim retlist As New List(Of String)
        For i As Integer = 0 To upto
            If Not skip.Contains(i) Then
                retlist.Add(i.ToString)
            End If
        Next

        Return retlist
    End Function





    Private Sub DisableAll()
        TrophyEnabled = False
        For Each i As CheckBox In CheckBoxList
            If Not i.Checked Then
                i.Enabled = False
            End If
        Next
    End Sub
    Private Sub EnableAll()
        TrophyEnabled = True
        For Each i As CheckBox In CheckBoxList
            i.Enabled = True
        Next
    End Sub


    Private Sub TrophyButton_CheckedChanged(sender As Object, e As EventArgs) Handles Trophy0.CheckedChanged, Trophy1.CheckedChanged, Trophy2.CheckedChanged, Trophy3.CheckedChanged,
            Trophy4.CheckedChanged, Trophy5.CheckedChanged, Trophy6.CheckedChanged, Trophy7.CheckedChanged, Trophy8.CheckedChanged, Trophy9.CheckedChanged
        CheckIfAllFilled()
        UpdateUI()
    End Sub
    Private Sub CheckIfAllFilled()
        If GetCurrentlySelected() >= TotalTrophies Then
            DisableAll()
        Else
            EnableAll()
        End If
        checkLineFilled()

    End Sub
    Public Function AllChecked(ListOf As List(Of CheckBox)) As Boolean
        For Each I As CheckBox In ListOf
            If Not I.Checked Then
                Return False
            End If
        Next
        Return True
    End Function



    Private Sub checkLineFilled()
        For Each Pair As KeyValuePair(Of CheckBox, List(Of CheckBox)) In MapCheckBox
            If AllChecked(Pair.Value) AndAlso Pair.Key.Checked = False Then
                DoNotChange = True
                Pair.Key.Checked = True
            ElseIf Pair.Key.Checked AndAlso Not AllChecked(Pair.Value) Then
                DoNotChange = True
                Pair.Key.Checked = False
            End If
        Next
    End Sub

    Private Sub SaveToSheet_Click(sender As Object, e As EventArgs) Handles SaveToSheet.Click
        SaveToWrapper
    End Sub
    Private Function GetListSelected() As List(Of String)
        Dim retlist As New List(Of String)
        For i = 0 To CheckBoxList.Count - 1
            If CheckBoxList(i).Checked Then
                retlist.Add(i.ToString)
            End If
        Next
        Return retlist
    End Function
    Private Sub SaveToWrapper()
        Me.TROPHY_LIMITER = GetListSelected()
        UpdateUI()
        Me.DialogResult = DialogResult.OK
        Close()
    End Sub
End Class