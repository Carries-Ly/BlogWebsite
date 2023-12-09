// Function to handle responses
function handleResponse(response) {
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response;
}

// GET request
export function getRequest(url) {
  return fetch(url)
    .then(handleResponse)
    .then(response => response.json()) // Assuming the response is JSON
    .catch(error => {
      console.error("Fetch error: ", error);
    });
}

// POST request
export function postRequest(url, data) {
  return fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(handleResponse)
    .then(response => response.json()) // Assuming the response is JSON
    .catch(error => {
      console.error("Fetch error: ", error);
    });
}