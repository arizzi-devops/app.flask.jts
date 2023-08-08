// Define global variables to store current jobId and statusId
var jobId = null;
var statusId = null;

function isSameColumn(sourceColumnId, targetColumnId) {
  return sourceColumnId === targetColumnId;
}

// Drag and Drop Functions
function allowDrop(event) {
  event.preventDefault();
}

function drag(event) {
  event.currentTarget.classList.add("dragging");
  jobId = $(event.target).closest(".card.mb-3").attr("data-task-id");
  statusId = $(event.target).closest(".card.mb-3").closest(".card-body").attr("data-column-id");
}

function drop(event) {
  event.preventDefault();
  var targetColumnId = event.currentTarget.getAttribute("data-column-id");
  var targetColumn = $(event.currentTarget);

  if (isSameColumn(statusId, targetColumnId)) {
    console.log('Same column, skipping request');
    return;
  }

  // Move the dragged task to the target column
  var task = $("[data-task-id='" + jobId + "']");
  targetColumn.append(task);

  // Update the task's data-column-id attribute
  task.attr("data-column-id", targetColumnId);

  // Perform AJAX request to update the job status
  $.ajax({
    url: "/jobs/edit/" + jobId + "/status",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      new_status_id: targetColumnId,
    }),
    success: function(response) {
      console.log("Job status updated successfully.");
    },
    error: function(xhr, status, error) {
      console.error("An error occurred while updating the job status:", error);
    }
  });

  // Reset the jobId and statusId variables
  jobId = null;
  statusId = null;
}

$(document).ready(function() {
  $(".card.mb-3").on("dblclick", function(event) {
    var jobId = $(this).attr("data-task-id");
    window.location.href = "/jobs/edit/" + jobId;
  });

  // Add dragend event listener to remove 'dragging' class
  $(".card.mb-3").on("dragend", function(event) {
    event.currentTarget.classList.remove("dragging");
  });

  // Set draggable property for cards with class "card mb-3"
  $(".card.mb-3").each(function() {
    $(this).attr("draggable", "true");
  });

  // Add dragstart event listener to cards
  $(".card.mb-3").on("dragstart", drag);

  // Add dragover and drop event listeners to columns
  $(".card[data-column-id]").on("dragover", allowDrop);
  $(".card[data-column-id]").on("drop", drop);
});
