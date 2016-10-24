<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class ChangeForm
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.NameTextBox = New System.Windows.Forms.TextBox()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.YearTextBox = New System.Windows.Forms.TextBox()
        Me.ChangeToRow = New System.Windows.Forms.Button()
        Me.CancelFromRow = New System.Windows.Forms.Button()
        Me.Plaque_BUTTON = New System.Windows.Forms.RadioButton()
        Me.Trophy_BUTTON = New System.Windows.Forms.RadioButton()
        Me.SuspendLayout()
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(12, 39)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(35, 13)
        Me.Label1.TabIndex = 8
        Me.Label1.Text = "Name"
        '
        'NameTextBox
        '
        Me.NameTextBox.Location = New System.Drawing.Point(56, 36)
        Me.NameTextBox.Name = "NameTextBox"
        Me.NameTextBox.Size = New System.Drawing.Size(157, 20)
        Me.NameTextBox.TabIndex = 7
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(18, 83)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(29, 13)
        Me.Label2.TabIndex = 9
        Me.Label2.Text = "Year"
        '
        'YearTextBox
        '
        Me.YearTextBox.Location = New System.Drawing.Point(56, 80)
        Me.YearTextBox.Name = "YearTextBox"
        Me.YearTextBox.Size = New System.Drawing.Size(157, 20)
        Me.YearTextBox.TabIndex = 10
        '
        'ChangeToRow
        '
        Me.ChangeToRow.Location = New System.Drawing.Point(219, 34)
        Me.ChangeToRow.Name = "ChangeToRow"
        Me.ChangeToRow.Size = New System.Drawing.Size(75, 23)
        Me.ChangeToRow.TabIndex = 11
        Me.ChangeToRow.Text = "Change"
        Me.ChangeToRow.UseVisualStyleBackColor = True
        '
        'CancelFromRow
        '
        Me.CancelFromRow.DialogResult = System.Windows.Forms.DialogResult.Cancel
        Me.CancelFromRow.Location = New System.Drawing.Point(219, 78)
        Me.CancelFromRow.Name = "CancelFromRow"
        Me.CancelFromRow.Size = New System.Drawing.Size(75, 23)
        Me.CancelFromRow.TabIndex = 12
        Me.CancelFromRow.Text = "Cancel"
        Me.CancelFromRow.UseVisualStyleBackColor = True
        '
        'Plaque_BUTTON
        '
        Me.Plaque_BUTTON.AutoSize = True
        Me.Plaque_BUTTON.Location = New System.Drawing.Point(160, 106)
        Me.Plaque_BUTTON.Name = "Plaque_BUTTON"
        Me.Plaque_BUTTON.Size = New System.Drawing.Size(118, 17)
        Me.Plaque_BUTTON.TabIndex = 14
        Me.Plaque_BUTTON.Text = "SCHOOL_PLAQUE"
        Me.Plaque_BUTTON.UseVisualStyleBackColor = True
        '
        'Trophy_BUTTON
        '
        Me.Trophy_BUTTON.AutoSize = True
        Me.Trophy_BUTTON.Checked = True
        Me.Trophy_BUTTON.Location = New System.Drawing.Point(24, 106)
        Me.Trophy_BUTTON.Name = "Trophy_BUTTON"
        Me.Trophy_BUTTON.Size = New System.Drawing.Size(120, 17)
        Me.Trophy_BUTTON.TabIndex = 13
        Me.Trophy_BUTTON.TabStop = True
        Me.Trophy_BUTTON.Text = "SCHOOL_TROPHY"
        Me.Trophy_BUTTON.UseVisualStyleBackColor = True
        '
        'ChangeForm
        '
        Me.AcceptButton = Me.ChangeToRow
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.CancelButton = Me.CancelFromRow
        Me.ClientSize = New System.Drawing.Size(334, 141)
        Me.Controls.Add(Me.Plaque_BUTTON)
        Me.Controls.Add(Me.Trophy_BUTTON)
        Me.Controls.Add(Me.CancelFromRow)
        Me.Controls.Add(Me.ChangeToRow)
        Me.Controls.Add(Me.YearTextBox)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.NameTextBox)
        Me.Name = "ChangeForm"
        Me.Text = "ChangeForm"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents Label1 As Label
    Friend WithEvents NameTextBox As TextBox
    Friend WithEvents Label2 As Label
    Friend WithEvents YearTextBox As TextBox
    Friend WithEvents ChangeToRow As Button
    Friend WithEvents CancelFromRow As Button
    Friend WithEvents Plaque_BUTTON As RadioButton
    Friend WithEvents Trophy_BUTTON As RadioButton
End Class
