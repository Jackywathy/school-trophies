Public Class AddForm
    Dim retList As List(Of String)
    Private Sub AddToRow_Click(sender As Object, e As EventArgs) Handles AddToRow.Click
        Dim YearInt As Integer
        retList = New List(Of String)
        If NameTextBox.Text <> String.Empty And YearTextBox.Text <> String.Empty Then
            If Integer.TryParse(YearTextBox.Text, YearInt) <> Nothing Then
                ' valid int
                If Trophy_BUTTON.Checked = True Then
                    retList.Add("SCHOOL_TROPHY")
                Else
                    retList.Add("SCHOOL_PLAQUE")
                End If
                retList.Add(NameTextBox.Text)
                retList.Add(YearTextBox.Text)
                Me.DialogResult = DialogResult.OK
                Close()
            Else
                MsgBox("Please Enter a valid Int")
            End If
        Else
            MsgBox("Please input values in both Name and Year")
        End If
    End Sub

    Public Function GetTextRow() As List(Of String)
        Return retList
    End Function
    Private Sub CancelFromRow_Click(sender As Object, e As EventArgs) Handles CancelFromRow.Click
        Me.DialogResult = DialogResult.Cancel
        Close()
    End Sub

    Private Sub AddForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub
End Class