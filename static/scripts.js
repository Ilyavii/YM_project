$(function () {
    // Your existing code...

    // Add this block to handle the download button click
    $('#downloadBtn').on('click', function () {
        var selectedRows = $table.bootstrapTable('getSelections');

        if (selectedRows.length > 0) {
            // Create a CSV string from the selected rows
            var csvContent = "data:text/csv;charset=utf-8,"
                + selectedRows.map(row => Object.values(row).join(',')).join('\n');

            // Create a download link and trigger the download
            var encodedUri = encodeURI(csvContent);
            var link = document.createElement("a");
            link.setAttribute("href", encodedUri);
            link.setAttribute("download", "selected_rows.csv");
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        } else {
            // Inform the user if no rows are selected
            alert('No rows selected for download.');
        }
    });
});
