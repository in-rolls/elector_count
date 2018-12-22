import tarfile
from pdfrw import PdfReader

def total_pdf_pages_in_tar_gz(tfn):
    tar = tarfile.open(tfn, "r:gz")
    errors = {}
    pages = {}
    for i, tarinfo in enumerate(tar):
        name = tarinfo.name
        name = name.split('/')[-1]
        if tarinfo.isreg():
            member = tar.getmember(tarinfo.name)
            try:
                f = tar.extractfile(member)
                pdf = PdfReader(f)
                count = len(pdf.pages)
                pages[name] = count
            except Exception as e:
                pages[name] = 0
                msg = e.msg
                if msg in errors:
                    errors[msg] += 1
                else:
                    errors[msg] = 1
            finally:
                f.close()
        elif tarinfo.isdir():
            pass
        else:
            print("something else.")

    return (pages, errors)


if __name__ == "__main__":

    files, errors = total_pdf_pages_in_tar_gz("sample_pdfs.tar.gz")

    print("files:", len(files))

    print("errors:", errors)

    count = 0
    for p in files:
        count += files[p]
    print("pages: {:d}".format(count))
