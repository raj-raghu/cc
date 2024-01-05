document.addEventListener("DOMContentLoaded", function() {
    setupEditableCells();
    highlightKeywords();
});

function setupEditableCells() {
    const editableCells = document.querySelectorAll('.editable');
    editableCells.forEach(cell => {
        cell.addEventListener('input', function() {
            // Handle cell value update here
            console.log('Cell value updated:', this.textContent);
        });
    });
}

function highlightKeywords() {
    const jobRow = document.querySelector('.job-row');

    const allTextCell = jobRow.querySelector('.editable[data-column="AllText"]');
    if (allTextCell) {
        const cellContents = allTextCell.innerText;
        const highlightedContents = cellContents.replace(/KEY RESPONSIBILITIES/g, '<span class="highlight">KEY RESPONSIBILITIES</span>');
        allTextCell.innerHTML = highlightedContents;
    }
}


