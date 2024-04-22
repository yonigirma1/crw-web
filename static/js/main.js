$("#id_transcript_file").change(function () {
  let files = $("#id_transcript_file")[0].files;
  if (files.length) {
    $("#filename1").text(files[0].name);
  } else {
    $("#filename1").html(`Drag a Photo or <br>
    <span class="text-primary">Browse</span>`);
  }
});

$("#id_id_file").change(function () {
  let files = $("#id_id_file")[0].files;
  if (files.length) {
    $("#filename2").text(files[0].name);
  } else {
    $("#filename2").html(`Drag a Photo or <br>
    <span class="text-primary">Browse</span>`);
  }
});

$("#id_application_file").change(function () {
  let files = $("#id_application_file")[0].files;
  if (files.length) {
    $("#filename3").text(files[0].name);
  } else {
    $("#filename3").html(`Drag a Photo or <br>
    <span class="text-primary">Browse</span>`);
  }
});

$("#id_driver_license_file").change(function () {
  let files = $("#id_driver_license_file")[0].files;
  if (files.length) {
    $("#filename4").text(files[0].name);
  } else {
    $("#filename4").html(`Drag a Photo or <br>
    <span class="text-primary">Browse</span>`);
  }
});

$("#id_medical_card_file").change(function () {
  let files = $("#id_medical_card_file")[0].files;
  if (files.length) {
    $("#filename5").text(files[0].name);
  } else {
    $("#filename5").html(`Drag a Photo or <br>
    <span class="text-primary">Browse</span>`);
  }
});

$("#id_birth_certificate_file").change(function () {
  let files = $("#id_birth_certificate_file")[0].files;
  if (files.length) {
    $("#filename6").text(files[0].name);
  } else {
    $("#filename6").html(`Drag a Photo or <br>
    <span class="text-primary">Browse</span>`);
  }
});

$("#id_drug_screening_file").change(function () {
  let files = $("#id_drug_screening_file")[0].files;
  if (files.length) {
    $("#filename7").text(files[0].name);
  } else {
    $("#filename7").html(`Drag a Photo or <br>
    <span class="text-primary">Browse</span>`);
  }
});

$("#id_miscellaneous_file").change(function () {
  let files = $("#id_miscellaneous_file")[0].files;
  if (files.length) {
    $("#filename8").text(files[0].name);
  } else {
    $("#filename8").html(`Drag a Photo or <br>
    <span class="text-primary">Browse</span>`);
  }
});
