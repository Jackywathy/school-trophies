Public Class ChangeForm
    Dim retList As ArrayList
    Dim RowInteger As Integer
    Public Sub FillForm(RowInteger As Integer, AwardType As String, Name As String, Year As String)
        NameTextBox.Text = Name
        YearTextBox.Text = Year
        Me.RowInteger = RowInteger
        If AwardType = "SCHOOL_TROPHY" Then
            Trophy_BUTTON.Checked = True
            Plaque_BUTTON.Checked = False
        ElseIf AwardType = "SCHOOL_PLAQUE" Then
            Trophy_BUTTON.Checked = False
            Plaque_BUTTON.Checked = True
        End If
    End Sub

    Private Sub AddToRow_Click(sender As Object, e As EventArgs) Handles ChangeToRow.Click
        Dim CurrentType As String
        If Trophy_BUTTON.Checked Then
            CurrentType = "SCHOOL_TROPHY"
        ElseIf Plaque_BUTTON.Checked Then
            CurrentType = "SCHOOL_PLAQUE"
        Else
            Throw New Exception("type is not eqyal to trophy or plaqye?")
        End If
        retList = New ArrayList
        retList.Add(RowInteger)
        retList.AddRange(New String() {CurrentType, NameTextBox.Text, YearTextBox.Text})
        Me.DialogResult = DialogResult.OK
        Close()
    End Sub

    Private Sub CancelFromRow_Click(sender As Object, e As EventArgs) Handles CancelFromRow.Click
        Me.DialogResult = DialogResult.Cancel
        Close()
    End Sub
    Public Function GetEditItem() As ArrayList
        Return retList
    End Function

    Private Sub ChangeForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub
End Class