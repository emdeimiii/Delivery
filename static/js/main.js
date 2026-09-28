
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        document.querySelectorAll('.btn-add').forEach(button => {
            button.addEventListener('click', function() {
                this.innerHTML = '<i class="bi bi-check"></i> Добавлено';
                this.style.backgroundColor = '#28a745';
                setTimeout(() => {
                    this.innerHTML = '<i class="bi bi-plus"></i> Добавить';
                    this.style.backgroundColor = '';
                }, 2000);
            });
        });
